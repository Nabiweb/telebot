from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Movie recommendations by genre with release years and photos
MOVIE_RECOMMENDATIONS = {
    "Action": [
        {"name": "Baahubali", "year": 2015, "photo": "https://example.com/baahubali.jpg"},
        {"name": "KGF", "year": 2018, "photo": "https://example.com/kgf.jpg"},
        {"name": "Vikram", "year": 2022, "photo": "https://example.com/vikram.jpg"},
        {"name": "War", "year": 2019, "photo": "https://example.com/war.jpg"}
    ],
    "Romance": [
        {"name": "Dilwale Dulhania Le Jayenge", "year": 1995, "photo": "https://example.com/ddlj.jpg"},
        {"name": "Kabir Singh", "year": 2019, "photo": "https://example.com/kabir_singh.jpg"},
        {"name": "2 States", "year": 2014, "photo": "https://example.com/2_states.jpg"},
        {"name": "Yeh Jawaani Hai Deewani", "year": 2013, "photo": "https://example.com/yjhd.jpg"}
    ],
    "Comedy": [
        {"name": "Hera Pheri", "year": 2000, "photo": "https://example.com/hera_pheri.jpg"},
        {"name": "3 Idiots", "year": 2009, "photo": "https://example.com/3_idiots.jpg"},
        {"name": "Chup Chup Ke", "year": 2006, "photo": "https://example.com/chup_chup_ke.jpg"},
        {"name": "Golmaal", "year": 2006, "photo": "https://example.com/golmaal.jpg"}
    ],
    "Drama": [
        {"name": "Masaan", "year": 2015, "photo": "https://example.com/masaan.jpg"},
        {"name": "The Lunchbox", "year": 2013, "photo": "https://example.com/lunchbox.jpg"},
        {"name": "Pink", "year": 2016, "photo": "https://example.com/pink.jpg"},
        {"name": "Gully Boy", "year": 2019, "photo": "https://example.com/gully_boy.jpg"}
    ],
    "Thriller": [
        {"name": "Andhadhun", "year": 2018, "photo": "https://example.com/andhadhun.jpg"},
        {"name": "Drishyam", "year": 2015, "photo": "https://example.com/drishyam.jpg"},
        {"name": "Talaash", "year": 2012, "photo": "https://example.com/talaash.jpg"},
        {"name": "Kahaani", "year": 2012, "photo": "https://example.com/kahaani.jpg"}
    ],
    "Horror": [
        {"name": "Tumbbad", "year": 2018, "photo": "https://example.com/tumbbad.jpg"},
        {"name": "Pari", "year": 2018, "photo": "https://example.com/pari.jpg"},
        {"name": "Bhoot", "year": 2020, "photo": "https://example.com/bhoot.jpg"},
        {"name": "Stree", "year": 2018, "photo": "https://example.com/stree.jpg"}
    ],
}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(genre, callback_data=genre)] for genre in MOVIE_RECOMMENDATIONS.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to the nabi's Movie Recommendation Bot!\n\nChoose a genre to get started:",
        reply_markup=reply_markup
    )

# Callback query handler for genre selection
async def recommend_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    genre = query.data
    if genre in MOVIE_RECOMMENDATIONS:
        movies = MOVIE_RECOMMENDATIONS[genre]
        media_group = [
            InputMediaPhoto(media=movie['photo'], caption=f"🎥 {movie['name']} ({movie['year']})") for movie in movies
        ]
        await context.bot.send_media_group(chat_id=query.message.chat_id, media=media_group)
        await query.edit_message_text(f"You selected *{genre}*! Here are all the movies in this genre with their posters:", parse_mode="Markdown")
    else:
        await query.edit_message_text("Invalid selection.")

# Main function to start the bot
if __name__ == "__main__":
    import random
    import os

    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    BOT_TOKEN = "7917642093:AAHMRlPaqzJXbKel_5riuckZzoMpsaAPSDw"

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(recommend_movie))

    print("Bot is running...")
    application.run_polling()

