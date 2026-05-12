import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# -----------------------------------------------------------------------------
# Data Layer (Capa de Datos) | def = 1
# -----------------------------------------------------------------------------
# Using '@st.cache_data' to cache the loaded data for better performance.
@st.cache_data
# -----------------------------------------------------------------------------
def load_population_data(
    file_path: str = "data/quarterly_canada_population.csv",
) -> pd.DataFrame:
    """Load population data from file.

    Args:
        filepath: Path to the CSV file with quarterly population data.

    Returns:
        DataFrame with quarterly population data.

    Raises:
        FileNotFoundError: If the CSV file does not exist at the given path.
        ValueError: If the file is empty or cannot be parsed as a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(
            f"Data file not found at: '{file_path}'. Check the path and try again."
        )
        st.stop()
    except Exception as exc:
        st.error(f"Unexpected error loading data: {exc}")
        st.stop()

    if df.empty:
        st.error("The loaded data file is empty.")
        st.stop()

    return df


# -----------------------------------------------------------------------------
# Validation Layer (Capa de Validación) | def = 1 + 2 = 3
# -----------------------------------------------------------------------------
# Using an explicit mapping makes the intent clear and removes the fragility.
QUARTER_ORDER: dict[str, int] = {"Q1": 1, "Q2": 2, "Q3": 3, "Q4": 4}


def validate_date_range(
    start_year: int, start_q: str, end_year: int, end_q: str
) -> bool:
    """Check that the selected date range is chronologically valid.

    Args:
        start_year: The starting year (e.g. 1991).
        start_q: The starting quarter (e.g. "Q1").
        end_year: The ending year (e.g. 2023).
        end_q: The ending quarter (e.g. "Q4").

    Returns:
        True if the range is valid, False otherwise.
        Displays an st.error() message when invalid.
    """
    if start_year > end_year:
        st.error("Invalid range: 'Start Year' must come before 'End Year'.")
        return False

    if start_year == end_year:
        if QUARTER_ORDER[start_q] >= QUARTER_ORDER[end_q]:
            st.error("Invalid range: 'Start Quarter' must come before 'End Quarter'.")
            return False
    return True


def validate_row_exists(df: pd.DataFrame, quarter_label: str, role: str) -> bool:
    """Check that the given quarter label exists in the dataset.

    Args:
        df: The full population DataFrame.
        quarter_label: Label to look up (e.g. 'Q3 1991').
        role: Human-readable description ('Start date' or 'End date') for error messages.

    Returns:
        True if the label is found, False otherwise.
    """
    if quarter_label not in df["Quarter"].values:
        st.error(f"{role} '{quarter_label}' is not available in the dataset.")
        return False
    return True


# -----------------------------------------------------------------------------
# Computation Layer (Capa de Cómputo) | def = 3 + 2 = 5
# -----------------------------------------------------------------------------
def compute_population_delta(start_value: float, end_value: float) -> float:
    """Calculate the percentage between two population values.

    Args:
        start_value: Population at the start date.
        end_value: Population at the end date.

    Returns:
        Percentage change a a float (e.g. 0.23 means +23%).
        Returns float('nan') if start_value is zero to avoid ZeroDivisionError.
    """
    if start_value == 0:
        return float("nan")
    return (end_value - start_value) / start_value


def get_filtered_df(df: pd.DataFrame, start_label: str, end_label: str) -> pd.DataFrame:
    """Slice the DataFrame to the selected date range (inclusive).

    Args:
        df: The full population DataFrame.
        start_label: Quarter label for the start row (e.g. 'Q3 1991')
        end_label: Quarter label for the end row (e.g. 'Q4 2023').

    Returns:
        A DataFrame slice covering [start_label, end_label].
    """
    start_index = df.loc[df["Quarter"] == start_label].index.item()
    end_index = df.loc[df["Quarter"] == end_label].index.item()
    return df.iloc[start_index : end_index + 1]


# -----------------------------------------------------------------------------
# Visualization Layer (Capa de Visualización) | def = 5 + 2 = 7
# -----------------------------------------------------------------------------
def plot_population_trend(filtered_df: pd.DataFrame, location: str) -> plt.Figure:
    """Generate a line chart of population over time for a single location.

    Args:
        filtered_df: Filtered DataFrame covering the selected date range.
        location: Column name representing the geographic region.

    Returns:
        Matplotlib Figure object ready to pass to st.pyplot().
    """
    fig, ax = plt.subplots()
    ax.plot(filtered_df["Quarter"], filtered_df[location])
    ax.set_title(location)
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Population")
    ax.set_xticks([filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]])
    fig.autofmt_xdate()
    return fig


def plot_comparison_trend(
    filtered_df: pd.DataFrame, locations: list[str]
) -> plt.Figure:
    """Generate a multi-line chart comparing population across locations.

    Args:
        filtered_df: Filtered DataFrame covering the selected date range.
        locations: List of column names (regions) to plot simultaneously.

    Regurns:
        Matplotlib Figure object ready to pass to st.pyplot().
    """

    fig, ax = plt.subplots()
    for loc in locations:
        ax.plot(filtered_df["Quarter"], filtered_df[loc], label=loc)
    ax.set_title("Population Comparison")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Population")
    ax.set_xticks([filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]])
    ax.legend()
    fig.autofmt_xdate()
    return fig


# -----------------------------------------------------------------------------
# User Interface Layer (Capa de Interfaz de Usuario) | def = 7 + 4 = 11
# -----------------------------------------------------------------------------
def render_header() -> None:
    """Render the app header section."""
    st.title("Claude Bootcamp - Sprint 1")
    st.subheader("Refactored Capstone Project #1 - Population of Canada")
    st.write(
        "Source table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)"
    )
    st.divider()


def render_data_preview(df: pd.DataFrame) -> None:
    """Render colapsible preview of the full dataset.

    Args:
        df: The full population DataFrame.
    """
    with st.expander("see full data table"):
        st.dataframe(df)


def render_input_form(df: pd.DataFrame) -> tuple[str, int, str, int, str, bool]:
    """Render the date range and location selection form.

    Args:
        df: The full population DataFrame (used to extract location options).

    Returns:
        Tuple of (start_q, start_year, end_q, end_year, location, form_submitted).
    """
    with st.form("population_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Choose a starting date")
            start_q = st.selectbox(
                "Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q"
            )
            start_year = st.slider(
                "Year",
                min_value=1991,
                max_value=2023,
                value=1991,
                step=1,
                key="start_year",
            )

        with col2:
            st.write("Choose an end date")
            end_q = st.selectbox(
                "Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=0, key="end_q"
            )
            end_year = st.slider(
                "Year",
                min_value=1991,
                max_value=2023,
                value=2023,
                step=1,
                key="end_year",
            )

        with col3:
            st.write("Choose a location")
            location = st.selectbox(
                "Location", options=df.columns[1:].to_list(), index=0, key="location"
            )

        submitted = st.form_submit_button("Analyze", type="primary")

    return start_q, start_year, end_q, end_year, location, submitted


def render_results(
    df: pd.DataFrame, start_label: str, end_label: str, location: str
) -> None:
    """Render the population change and compare tabs.

    Args:
        df: The full population DataFrame.
        start_label: Selected start quarter label (e.g. 'Q3 1991').
        end_label: Selected end quarter label (e.g. 'Q4 2023').
        location: Selected geographic region (column name).
    """
    filtered_df = get_filtered_df(df, start_label, end_label)
    result_start = df.loc[df["Quarter"] == start_label, location].values[0]
    result_end = df.loc[df["Quarter"] == end_label, location].values[0]
    delta = compute_population_delta(result_start, result_end)

    tab1, tab2 = st.tabs(["Population Change", "Compare"])
    with tab1:
        st.subheader(f"Population change: {start_label} -> {end_label} ({location})")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=start_label, value=f"{result_start:,}")
            delta_display = (
                f"{delta:.2%}" if not pd.isna(delta) else "N/A (start value is 0)"
            )
            st.metric(label=end_label, value=f"{result_end:,}", delta=delta_display)

        with col2:
            st.pyplot(plot_population_trend(filtered_df, location))

    with tab2:
        st.subheader("Compare with other locations")
        selected_locations = st.multiselect(
            "Choose locations to compare",
            options=df.columns[1:].tolist(),
            default=[location],
        )

        if selected_locations:
            st.pyplot(plot_comparison_trend(filtered_df, selected_locations))


# -----------------------------------------------------------------------------
# Entrypoint | def = 11 + 1 = 12
# -----------------------------------------------------------------------------
def main() -> None:
    """Main application entrypoint."""

    render_header()
    df = load_population_data()
    render_data_preview(df)

    start_q, start_year, end_q, end_year, location, submitted = render_input_form(df)

    start_label = f"{start_q} {start_year}"
    end_label = f"{end_q} {end_year}"

    is_valid = validate_date_range(start_year, start_q, end_year, end_q)

    if is_valid:
        is_valid = validate_row_exists(df, start_label, "Start date")
    if is_valid:
        is_valid = validate_row_exists(df, end_label, "End date")
    if is_valid:
        render_results(df, start_label, end_label, location)


if __name__ == "__main__":
    main()
