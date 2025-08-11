"""
Akash Shirodkar - Futuristic Flask Portfolio
--------------------------------------------
Flask application entry point for serving portfolio website pages.
"""

from flask import Flask, render_template
import os

# Create Flask app instance
app = Flask(
    __name__,
    template_folder="templates",  # adjust if templates are in a different directory
    static_folder="static"        # adjust if static files in folder named 'static'
)

# Home / Landing page
@app.route("/")
def home():
    """
    Render the main portfolio homepage.
    """
    return render_template("index.html")

# Optionally, you can have a custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom template.
    """
    return render_template("404.html"), 404

if __name__ == "__main__":
    # Get port from environment (useful for deployment platforms like Heroku)
    port = int(os.environ.get("PORT", 5000))
    
    # Enable/disable debug mode based on environment
    debug_mode = os.environ.get("FLASK_DEBUG", "1") == "1"
    
    app.run(
        host="0.0.0.0",  # Allows external access if running on a server
        port=port,
        debug=debug_mode
    )
