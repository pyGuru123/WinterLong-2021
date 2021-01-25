# WhatsApp ![Alt text](whatsapp_icon.png?raw=true "WhatsApp") Group Chat Analysis

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

This notebook analyses a exported .txt chat file of science & technology based whatsapp group. To analyse your own chat .txt file, On your phone, go to the WhatsApp group and click the 3 dots in the top right. Then go to ‘More’ and to ‘Export chat’. Select omit media. You can then select where to save this.

## Aim & Observations

To Analyse group chats of a whatsapp group

The case study is divied into 10 parts:

1. Preprocessing chat text file : hiding phone numbers, converting multiline messages to single line.
2. Converting text file to Date, time - sender : message format.
3. Reading the text file as Pandas Dataframe, removing unwanted messages.
4. Extracting date, time, sender & message as seperate columns.
5. Extracting chat data info / group Insight
6. Visualize number of message by each member.
7. Visualize number of messages sent each day.
8. Visualize Most common messaging time.
9. Visualize Most common words
10. Visualize Most common used emojis

![Alt text](visualization.png?raw=true "Tracking Bird Migration")

## Dataset 

Used Dataset : Chat file exported from a Science & Technology based Whatsapp group.

To analyse your own chat .txt file, On your phone, go to the WhatsApp group and click the 3 dots in the top right. Then got to ‘More’ and to ‘Export chat’. Select omit media. You can then select where to save this.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages :-
* Calplot
* WordCloud
* Matplotlib
* Pandas

```bash
pip install Calplot
pip install WordCloud
pip install Matplotlib
pip install Pandas
```

To make most out of this project run it in google colab

## How to Download

Download this project from here [Download WhatsApp Group Chat Analysis](https://downgit.github.io/#/home?url=https://github.com/pyGuru123/Data-Analysis-and-Visualization/tree/main/WhatsApp%20Group%20Chat%20Analysis)

## Some interesting results


### Busiest Hours
![Alt text](plots/busiest_hours.png?raw=true "Busiest Hours")

### Calendar Map
![Alt text](plots/calendarmap.png?raw=true "CalendarMap")


### Message sent each weekday
![Alt text](plots/Message_sent_each_weekday.png?raw=true "Message sent each weekday")


### Most Common Words used
![Alt text](plots/most_common_words.png?raw=true "Most Common Words used")


### Most frequent used words
![Alt text](plots/most_frequent_wordcloud.png?raw=true "Most frequent wordcloud")


### Most popular hours
![Alt text](plots/most_popular_hours.png?raw=true "Most popular hours")

