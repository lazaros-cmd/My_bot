import os, threading
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = 8820635848:AAGUh41z1M9IBsMdxt57bke5PSgeWztLxNo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Γεια! Το bot σου τρέχει 24/7 στο Cloud!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Μου έγραψες: {update.message.text}")

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"OK")

def run_health_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), HealthCheckHandler)
    server.serve_forever()

def main():
    threading.Thread(target=run_health_server, daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()
  
