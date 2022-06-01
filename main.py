import Constans as keys
from telegram.ext import *
import Responses as 


print("Meowwwww Started....")


def start_command(update, context):
  update.message.reply_text('Type Something Random To Get Started')
  
  
  
  def help_command(update, context):
 update.message.reply_text('If you need help')
  
  def handle_command(update, context):
  text = str(update.message.text).lower()
  Response = R.sample_responses(text)
  
  
  update.message.reply_text(response)
  
  def error(update, context):
    print(f"update {update} caused error {context.error}")
    
    def main():
      updater = Updater(keys.API_KEY, use_context=True)
      dp = updater.dispatcher
      
      dp.add_handler(CommandHandler("start", start_command))
      dp.add_handler(CommandHandler("help", help_command))
      
      dp.add_handler(MessageHandler(Filters.text, handle_message))
      
      
      dp.add_error_handler(error)
            
      
      
      
      
      
      updater.start_polling(1)
      updater.idle()
      
      
      
      main()
      
      
      
      
