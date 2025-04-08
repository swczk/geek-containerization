mod stardate;
mod api;
mod error;

use rocket::Config;
use std::net::Ipv4Addr;

#[rocket::main]
async fn main() -> Result<(), rocket::Error> {
    let config = Config {
        address: Ipv4Addr::new(0, 0, 0, 0).into(),
        port: 8000,
        ..Config::default()
    };

    rocket::custom(config)
        .mount("/", api::routes())
        .launch()
        .await?;

    Ok(())
}
