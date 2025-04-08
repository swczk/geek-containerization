use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::{get, post, routes};
use chrono::{DateTime, Utc, NaiveDateTime};

use crate::error::StardateError;
use crate::stardate::{Stardate, StardateSystem};

#[derive(Serialize)]
#[serde(crate = "rocket::serde")]
pub struct ApiResponse<T> {
    success: bool,
    data: Option<T>,
    error: Option<String>,
}

#[derive(Serialize)]
#[serde(crate = "rocket::serde")]
pub struct StardateResponse {
    earth_date: String,
    stardates: Vec<StardateInfo>,
}

#[derive(Serialize)]
#[serde(crate = "rocket::serde")]
pub struct StardateInfo {
    system: String,
    stardate: f64,
    description: String,
}

#[derive(Deserialize)]
#[serde(crate = "rocket::serde")]
pub struct DateRequest {
    date: String,
}

#[get("/")]
fn index() -> Json<ApiResponse<String>> {
    Json(ApiResponse {
        success: true,
        data: Some("Welcome to the Stardate Converter. Use /api/stardate or /api/current to convert dates.".into()),
        error: None,
    })
}

#[get("/api/systems")]
fn get_systems() -> Json<ApiResponse<Vec<String>>> {
    let systems = vec![
        "TOS - The Original Series".to_string(),
        "TNG - The Next Generation".to_string(),
        "Kelvin - 2009 Movies".to_string(),
        "Discovery - Star Trek: Discovery".to_string(),
    ];

    Json(ApiResponse {
        success: true,
        data: Some(systems),
        error: None,
    })
}

#[get("/api/current")]
fn get_current() -> Json<ApiResponse<StardateResponse>> {
    let now = Utc::now();
    match calculate_all_stardates(&now) {
        Ok(response) => Json(ApiResponse {
            success: true,
            data: Some(response),
            error: None,
        }),
        Err(e) => Json(ApiResponse {
            success: false,
            data: None,
            error: Some(e.to_string()),
        }),
    }
}

#[post("/api/stardate", format = "application/json", data = "<date_request>")]
fn convert_date(date_request: Json<DateRequest>) -> Json<ApiResponse<StardateResponse>> {
    match parse_date(&date_request.date) {
        Ok(date) => {
            match calculate_all_stardates(&date) {
                Ok(response) => Json(ApiResponse {
                    success: true,
                    data: Some(response),
                    error: None,
                }),
                Err(e) => Json(ApiResponse {
                    success: false,
                    data: None,
                    error: Some(e.to_string()),
                }),
            }
        },
        Err(e) => Json(ApiResponse {
            success: false,
            data: None,
            error: Some(format!("Invalid date format: {}", e)),
        }),
    }
}

fn parse_date(date_str: &str) -> Result<DateTime<Utc>, chrono::ParseError> {
    // Try several common formats
    let formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
    ];

    for format in formats.iter() {
        if let Ok(naive_datetime) = NaiveDateTime::parse_from_str(&format!("{} 00:00:00", date_str), &format!("{} %H:%M:%S", format)) {
            return Ok(DateTime::from_naive_utc_and_offset(naive_datetime, Utc));
        }
    }

    // If none of the formats work, try standard RFC3339 parse
    date_str.parse::<DateTime<Utc>>()
}

fn calculate_all_stardates(date: &DateTime<Utc>) -> Result<StardateResponse, StardateError> {
    let mut stardates = Vec::new();

    // TOS
    if let Ok(stardate) = Stardate::new(date, StardateSystem::TOS) {
        stardates.push(StardateInfo {
            system: stardate.system,
            stardate: stardate.date,
            description: stardate.description,
        });
    }

    // TNG
    if let Ok(stardate) = Stardate::new(date, StardateSystem::TNG) {
        stardates.push(StardateInfo {
            system: stardate.system,
            stardate: stardate.date,
            description: stardate.description,
        });
    }

    // Kelvin
    if let Ok(stardate) = Stardate::new(date, StardateSystem::Kelvin) {
        stardates.push(StardateInfo {
            system: stardate.system,
            stardate: stardate.date,
            description: stardate.description,
        });
    }

    // Discovery
    if let Ok(stardate) = Stardate::new(date, StardateSystem::Discovery) {
        stardates.push(StardateInfo {
            system: stardate.system,
            stardate: stardate.date,
            description: stardate.description,
        });
    }

    if stardates.is_empty() {
        return Err(StardateError::NoValidSystem);
    }

    Ok(StardateResponse {
        earth_date: date.to_rfc3339(),
        stardates,
    })
}

pub fn routes() -> Vec<rocket::Route> {
    routes![index, get_systems, get_current, convert_date]
}
