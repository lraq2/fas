@{username} - {score} زيارة\n"
    bot.send_message(message.chat.id, text)

# شرح طريقة البوت
@bot.message_handler(func=lambda message: message.text == "❓ طريقة استخدام البوت")
def how_to_use(message):
    bot.send_message(
        message.chat.id,
        "✨ هذا البوت يساعدك في:\n"
        "- 👤 معرفة من زار ملفك الشخصي.\n"
        "- 💌 معرفة الأشخاص الذين دعوتهم.\n"
        "- 📈 مشاهدة ترتيبك بين الأعضاء.\n\n"
        "🚀 استمر بدعوة أصدقائك للحصول على ترتيب أعلى!"
    )

# تعليمات وخطوات الدعوة
@bot.message_handler(func=lambda message: message.text == "📖 تعليمات وخطوات الدعوة")
def instructions(message):
    bot.send_message(
        message.chat.id,
        "🌟 **خطوات الدعوة والتفاعل مع البوت:**\n"
        "1️⃣ شارك رابط الدعوة الخاص بك مع أصدقائك.\n"
        "2️⃣ اجعلهم يشتركون في القناة الرسمية: [اضغط هنا]({CHANNEL_LINK}).\n"
        "3️⃣ عندما ينضم صديقك، ستزيد نقاط الدعوة لديك تلقائيًا.\n\n"
        "📊 كلما زادت نقاطك، ارتفع ترتيبك في الجترافي!",
        parse_mode="Markdown"
    )

# تشغيل البوت
if __name__ == "__main__":
    setup_database()
    bot.polling()
