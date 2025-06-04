from app import app, tracker, background_update
import threading

if __name__ == "__main__":
    # Start background update thread
    update_thread = threading.Thread(target=background_update, daemon=True)
    update_thread.start()
    
    # Initialize data
    tracker.update_historical_data()
    
    # Start app with gunicorn
    app.run()