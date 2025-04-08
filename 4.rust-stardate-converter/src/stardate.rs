use chrono::{DateTime, Datelike, Utc};
use rand::Rng;
use crate::error::StardateError;

/// The different stardate calculation systems in Star Trek
pub enum StardateSystem {
    /// The Original Series (TOS)
    TOS,
    /// The Next Generation (TNG), Deep Space Nine (DS9), Voyager
    TNG,
    /// Star Trek (2009) and sequels
    Kelvin,
    /// Star Trek: Discovery
    Discovery,
}

/// Representation of a stardate
#[derive(Debug, Clone)]
pub struct Stardate {
    pub date: f64,
    pub system: String,
    pub description: String,
}

impl Stardate {
    /// Creates a new stardate based on an Earth date and the chosen system
    pub fn new(date: &DateTime<Utc>, system: StardateSystem) -> Result<Self, StardateError> {
        match system {
            StardateSystem::TOS => calculate_tos_stardate(date),
            StardateSystem::TNG => calculate_tng_stardate(date),
            StardateSystem::Kelvin => calculate_kelvin_stardate(date),
            StardateSystem::Discovery => calculate_discovery_stardate(date),
        }
    }
}

/// Calculates stardate in Star Trek: The Original Series system
fn calculate_tos_stardate(date: &DateTime<Utc>) -> Result<Stardate, StardateError> {
    // Simplification based on year
    let year = date.year();

    if year < 1966 || year > 2270 {
        return Err(StardateError::OutOfRange);
    }

    // Initialize random number generator with seed based on date
    let mut rng = rand::thread_rng();

    // In TOS, stardates were somewhat inconsistent and random
    // Base of 1000.0 to 5999.9
    let base = rng.gen_range(1000.0..6000.0);

    // Adjustment based on year (further from 1966, higher the number)
    let year_factor = (year - 1966) as f64 * 0.7;

    let stardate = (base + year_factor).round() / 10.0;

    Ok(Stardate {
        date: stardate,
        system: "TOS".to_string(),
        description: "Stardate from Star Trek: The Original Series".to_string(),
    })
}

/// Calculates stardate in Star Trek: The Next Generation system
fn calculate_tng_stardate(date: &DateTime<Utc>) -> Result<Stardate, StardateError> {
    // TNG takes place from year 2364 to 2379
    let year = date.year();

    if year < 1987 || year > 2500 {
        return Err(StardateError::OutOfRange);
    }

    // In TNG, stardate follows a more consistent pattern
    // Format: [year]xxxx.x where xxxx.x represents the part of year

    // Convert Earth year to TNG year (assuming 2364 as year 41000)
    let tng_year = if year >= 2364 {
        // Actual year within TNG period
        41000 + (year - 2364)
    } else {
        // For current years, simulate as if we were in the future
        41000 + (year - 1987) / 5 // Slower scale
    };

    // Calculate decimal part based on day of year
    let day_of_year = date.ordinal() as f64;
    let day_decimal = day_of_year / 365.25;

    let stardate = tng_year as f64 + day_decimal * 1000.0;

    Ok(Stardate {
        date: (stardate * 10.0).round() / 10.0, // Round to 1 decimal place
        system: "TNG".to_string(),
        description: "Stardate from Star Trek: The Next Generation/DS9/Voyager".to_string(),
    })
}

/// Calculates stardate in Star Trek (2009) - Kelvin timeline
fn calculate_kelvin_stardate(date: &DateTime<Utc>) -> Result<Stardate, StardateError> {
    let year = date.year();

    if year < 2009 || year > 2500 {
        return Err(StardateError::OutOfRange);
    }

    // In the 2009 reboot, stardate uses format YYYYMM.DD
    let kelvin_year = if year >= 2233 {
        // Actual year within the movies' period
        year
    } else {
        // For current years, simulate as if we were in the future
        2233 + (year - 2009) / 4 // Slower scale
    };

    let month = date.month();
    let day = date.day();

    let stardate = kelvin_year as f64 * 100.0 + month as f64 + day as f64 / 100.0;

    Ok(Stardate {
        date: (stardate * 100.0).round() / 100.0, // Round to 2 decimal places
        system: "Kelvin".to_string(),
        description: "Stardate from the Kelvin timeline (Star Trek 2009)".to_string(),
    })
}

/// Calculates stardate in Star Trek: Discovery system
fn calculate_discovery_stardate(date: &DateTime<Utc>) -> Result<Stardate, StardateError> {
    let year = date.year();

    if year < 2017 || year > 3200 {
        return Err(StardateError::OutOfRange);
    }

    // Discovery initially takes place in 2256 (season 1)
    // and later in 3188 (season 3)
    let disc_year = if year >= 2256 {
        // Actual year within Discovery period
        year
    } else {
        // For current years, simulate as if we were in the future
        2256 + (year - 2017) / 4 // Slower scale
    };

    // In Discovery, the format seems to be simply the year followed by a number
    let day_of_year = date.ordinal() as f64;
    let day_decimal = day_of_year / 365.25 * 99.0; // 0-99 for the year

    let stardate = disc_year as f64 + day_decimal / 100.0;

    Ok(Stardate {
        date: (stardate * 100.0).round() / 100.0, // Round to 2 decimal places
        system: "Discovery".to_string(),
        description: "Stardate from Star Trek: Discovery".to_string(),
    })
}
