"""
Custom Gradio theme for Auralith to match a professional DAW's dark, industrial aesthetic.
"""
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

class AuralithTheme(Base):
    def __init__(self):
        super().__init__(
            primary_hue=colors.cyan,
            secondary_hue=colors.teal,
            neutral_hue=colors.slate,
            spacing_size=sizes.spacing_md,
            radius_size=sizes.radius_md,
            font=fonts.GoogleFont("Inter"),
        )
        self.name = "auralith_theme"
        self.set(
            # Colors
            body_background_fill="*neutral_900",
            body_background_fill_dark="*neutral_900",
            body_text_color="*neutral_50",
            body_text_color_dark="*neutral_50",

            background_fill_primary="*neutral_800",
            background_fill_primary_dark="*neutral_800",
            background_fill_secondary="*neutral_700",
            background_fill_secondary_dark="*neutral_700",

            border_color_accent="*primary_400",
            border_color_accent_dark="*primary_400",
            border_color_primary="*neutral_600",
            border_color_primary_dark="*neutral_600",

            color_accent_soft="*primary_700",
            color_accent_soft_dark="*primary_700",

            # Component-specific overrides
            button_primary_background_fill="linear-gradient(90deg, #48b5a3 0%, #2a8785 100%)",
            button_primary_background_fill_dark="linear-gradient(90deg, #48b5a3 0%, #2a8785 100%)",
            button_primary_text_color="white",
            button_primary_text_color_dark="white",

            slider_color="*primary_400",
            slider_color_dark="*primary_400",

            # Input fields
            input_background_fill="*neutral_700",
            input_background_fill_dark="*neutral_700",
            input_border_color="*neutral_600",
            input_border_color_dark="*neutral_600",
            input_placeholder_color="*neutral_300",
            input_placeholder_color_dark="*neutral_300",
        )

auralith_theme = AuralithTheme()

custom_css = """
/* --- Global Input Text Color --- */
.gradio-container .gr-input, .gradio-container .gr-textarea, .gradio-container .gr-dropdown {
    color: #ffffff !important; /* White text for all inputs */
}

.terminal-box textarea {
    background-color: #1a262c !important;
    color: #5ce1e6 !important; /* Lighter Turquoise Metallic */
    font-family: 'Courier New', monospace !important;
    border: 1px solid #2a8785 !important;
}
.main-header {
    text-align: center;
    margin-bottom: 20px;
    font-size: 2.5em;
    color: #ffffff;
    font-weight: bold;
}
/* Correctly target the slider's track fill for the progress bar effect */
.glowing-progress .track-fill {
    background-color: #5ce1e6 !important; /* Lighter Turquoise Metallic */
    box-shadow: 0 0 5px #5ce1e6, 0 0 10px #5ce1e6;
}
"""
