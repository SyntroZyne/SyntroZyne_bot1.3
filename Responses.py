from datetime import datetime

def sample_responses(input_text):
  user_message = str(input_text).lower()
  
  
  
  if user_message in ("hello", "hi", "sup", "how are you"):
    return "Hey !!!!!! How it's Goin?"
  
  
  if user_message in ("time", "time?"):
    now = datetime.now()
    datetime = now.strftime("%d/%m/%y, %h:%m:%s")
    return str(date_time)
  
  return " what?", "huh?", 
