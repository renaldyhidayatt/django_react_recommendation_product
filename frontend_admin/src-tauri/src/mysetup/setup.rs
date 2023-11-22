use tauri::{App, Manager};
use window_vibrancy::{self, NSVisualEffectMaterial};

pub fn init(app: &mut App) -> std::result::Result<(), Box<dyn std::error::Error>> {
    let win = app.get_window("main").unwrap();

    #[cfg(target_os = "macos")]
    window_vibrancy::apply_blur(&win, NSVisualEffectMaterial::FullScreenUI)
        .expect("Unsupported platform! 'apply_blur' is only supported on macOS");

    #[cfg(target_os = "windows")]
    window_vibrancy::apply_mica(&win, Some((18, 18, 18, 125)))
        .expect("Unsupported platform! 'apply_mica' is only supported on Windows");

    Ok(())
}
