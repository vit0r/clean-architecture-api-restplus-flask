from app import create_app

__all__ = (
    'create_app'
)

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, debug=True, port=3000)
