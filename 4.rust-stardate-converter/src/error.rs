use thiserror::Error;

#[derive(Error, Debug)]
pub enum StardateError {
    #[error("Date is outside the valid range for this system")]
    OutOfRange,

    #[error("No valid stardate system found for this date")]
    NoValidSystem,

    #[error("Error processing date: {0}")]
    ParseError(#[from] chrono::ParseError),
}
