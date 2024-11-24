from socketio import Server


def create_sio():
    # Create a Socket.IO server
    return Server(cors_allowed_origins="*", logger=False)  # Allow cross-origin requests
