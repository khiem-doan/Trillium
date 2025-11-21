
Good morning freeloaders. If you're seeing this you've been graced by the GOAT Khiem. Read the important first, then the general if you're wondering why certain functions aren't running or don't understand anything about the code. 

I am very sure the code works because it has worked for me and at least two other people. So that's nice. 

Also if the script works and you run it correctly it is gonna open a fuck ton of tabs. Be prepared to just exit chrome quick, but this is right. 

--------------------------------------------------------------------------------------------------------------
IMPORTANT
- news_scrape is the news scraper (duh)

- headers working is my short report scraper + my SEC scraper. 

TO RUN THE CODE
- run supervisor.py which should run headers + news scrape 
- In order to do so, you will have to download a lot of packages on Pycharm Community version. Install all of those (the list is literally on the top of headers, news scrape, and supervisor, so do that. If you fail to do this step it won't run, and you failed the IQ test. 
- if you want to run news scrape and headers at the same time, just run the supervisor script. That puts all the output into one big code output
  - But if you want to have separate code output for both, run headers, then run news scrape. It's your choice, but I find running supervisor saves me space
- If you ever see an error, STOP running the code immediately, comment out the specific thread that is running the error
  -For example, if white house is giving an error, comment out this: whitehouse_thread = threading.Thread(target=whitehouse_news) whitehouse_thread.start()
    - For my non coders put a hashtag in front of both of those lines
  - Then set the time.sleep at least a second greater for that whole code block
  - Only run the code again after a day or so for best results. But possibly wait more.
- In general on errors: The time frames I have are good to not get banned. If you see one off error messages once every few hours or so it's fine. But multiple errors in a row and you're in danger of being blocked. So some websites give me occassional errors that I ignore because it's fine, but be prudent for multiple.
- Once the whole code works, go to the bottom of this document. We want to have different user headers because if we all have the same user headers, the websites will detect that our IPs are running 3x or 4x as often, and increases the likelihood of being banned. So go down.


--------------------------------------------------------------------------------------------------------------

GENERAL
- On news scrape, you can run semafor_rohan but make sure that the time delay is not less than 3-4 seconds, I got blocked. Rohan Goswami is the only thing about Semafor that matters so far. 
- you can uncomment any of the threads to run them, just make sure you don't get blocked. I don't run some of them, but most should work.
- I believe I currently don't run culper and a few others, but try to un comment them and have fun. Will they work? Probably, idk, but if you start getting blocked, set the time.sleep for the whole function at least 1 second greater, don't run the code for a day or more, then try again.
- The sound alerts I downloaded manually. For you they will probably just be beeps. Download and save the sounds through Balbakoa and save them under the same name I have them as if you want them to work specifically - for example, for SEC 8ks, saying the word "SEC" instead of just beeping.
  - If you want to change the sounds you will have to change the file mapping in soundboard.py to wherever you have your sounds saved. It's really not the hardest thing in the world GPT 5.1 can probably help. 

--------------------------------------------------------------------------------------------------------------
OTHER SCRIPTS

- Ticker typing test is practicing pressing shift J twice if a ticker pops up. I use this for short reports getting fast asf.
- 13F live works for Nvidia and for berkshire. You are going to have to change the base file every quarter to compare against but it is fast asf
- The rest of the codes are really just tests, the tesla delivery one is not faster than bloomberg.







--------------------------------------------------------------------------------------------------------------
ONCE YOUR CODE WORKS FOR THE FIRST TIME

Nice, you passed the IQ test. 

You see the massive block that looks like this?

USER_AGENTS_DATA = [
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.1"},
    {"ua": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.2"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edge/132.0.0.0"},
    {"ua": "Mozilla/5.0 (Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.1 Safari/537.36 Opera/89.0.444.0"},
    {"ua": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36 Edge/127.1.1.1"},

.................................

Fantastic. 

Go to ChatGPT (or Gemini, idgaf) and ask AI to change this group of UAs to all different ones. Make it randomized and different.
Essentially we don't want to all be running the same user agents because it will detect that our browsers are all using the same stuff and increases ban likelihood. So change it up and copy your new list in. 

