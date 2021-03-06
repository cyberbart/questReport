import questRewardTypes
import questReward
import time
import datetime

class createMessage():

  def create(self,Sql,send,sleep,cfg,gmt,values):
    questType = questRewardTypes.rewardType()
    quest = questReward.reward()
    overview = ""
    bolt_line= ""

    stardust = values["stardust"]
    item = values["item"]
    pokemon = values["pokemon"]

    pokemon.sort(key=lambda x: quest.getPokemon(value=x))
    item.sort(key=lambda x: quest.getItem(value=x, icon="icon"))

    i = 0 # all found today quests
    x = 0 # all filtered quests
    id = 0    
    
    print("####################==========\\ " + str(datetime.datetime.now()) + " /==========####################\n")

    print("stardust melden: " + str(stardust))
    print("item ids melden: " + str(item))
    print("pokemon ids melden: " + str(pokemon))

    #return
    try:
      for stop in Sql.pokestop_id:
        name = "Unknown Pokestop" if Sql.name[i] is None else Sql.name[i]
        task = "\u2757 Aufgabe nicht bekannt" if Sql.quest_task[i] == "" else Sql.quest_task[i]

        if Sql.pokestop_id:
          if Sql.quest_stardust[i] in (stardust) or Sql.quest_item_id[i] in (item) or Sql.quest_pokemon_id[i] in (pokemon):

            ## STARDUST
            if not Sql.quest_stardust[i] == 0:
              bolt_line = "\u2728 <b>" + str(Sql.quest_stardust[i]) + " " + str(questType.getType(Sql.quest_reward_type[i])) + "</b>\n├ " + task
              if Sql.quest_stardust[i-1] != Sql.quest_stardust[i] and not Sql.quest_stardust[i] == Sql.quest_stardust[i+1]:
                msg = "\n" + str(bolt_line) + "\n└ "
                msg2= "\n"
              elif Sql.quest_stardust[i-1] != Sql.quest_stardust[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""
            
            ## ITEM
            elif Sql.quest_item_id[i] in (item):
              bolt_line = quest.getItem(Sql.quest_item_id[i],"icon") + " <b>" + str(Sql.quest_item_amount[i]) + " " + str(quest.getItem(Sql.quest_item_id[i], "name")) + "</b>\n├ " + task
              if Sql.quest_item_id[i-1] != Sql.quest_item_id[i] and not Sql.quest_item_id[i] == Sql.quest_item_id[i+1]:
                msg = "\n" + str(bolt_line) + "\n└ "
                msg2= "\n"
              elif Sql.quest_item_id[i-1] != Sql.quest_item_id[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""
            
            ## POKEMON
            elif Sql.quest_pokemon_id[i] in (pokemon):
              bolt_line = "\U0001F47E <b>" + str(quest.getPokemon(Sql.quest_pokemon_id[i])) + "</b>\n├ " + task
              if Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i] and not Sql.quest_pokemon_id[i] == Sql.quest_pokemon_id[i+1]:
                msg = "\n" + str(bolt_line) + "\n└ "
                msg2= "\n"
              elif Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""

            #singlemessage
            singlemessage = bolt_line.replace("├ ", "\U0001F4DC ")
            gmaps = "\n\n\U0001f4cd" + "<a href='https://maps.google.de/?q=" + str(Sql.latitude[i]) + "," + str(Sql.longitude[i]) + "'><b>" + name + "</b></a>\n" + singlemessage

            if send.list_output.__contains__(stop):
              f = open(cfg.areaName+"output.txt", "r")
                # Split the string based on space delimiter 
              list_string = f.read()
              list_string = list_string[1:len(list_string)-1]
              f.close()
              list_string = list_string.split(', ') 
              id = list_string[send.list_output.index(stop)]
            else:
              print("===> found [" + str(i) + "]")
              if cfg.singlechatId:
                id = send.send(gmaps,stop)
            if cfg.singlechatId:
              linked = cfg.singlechatUrl + "/" + str(id)
            else:
              linked = "https://maps.google.de/?q=" + str(Sql.latitude[i]) + ", " + str(Sql.longitude[i])
            overview += msg + "<a href='" + linked + "'>" + str(name) + "</a>" + msg2
            x +=1
          i +=1

      getWeekday =	{
        "Monday": "Montag",
        "Tuesday": "Dienstag",
        "Wednesday": "Mittwoch",
        "Thursday": "Donnerstag",
        "Friday": "Freitag",
        "Saturday": "Samstag",
        "Sunday": "Sonntag"
      }

      date = datetime.datetime.now()
      data = date.day,date.month,date.year
      weekday = getWeekday[date.strftime("%A")]

      header = "\U0001F4C6 " + str(weekday) + ", " + str(data[0]) + ". " + str(data[1]) + ". " + str(data[2]) + "\n(" + str(i-1) + " Stops wurden gescannt)\n"

      if not x == 0:
        send.sendOverview(header+overview)
      else:
        send.sendOverview(overview)
      print("\nAktuell " + str(x) + " Meldungen von " + str(i-1) + " Stops\n")

      # DEBUG:
      #f = open("TEST.txt", "a")
      #f.writelines("\n\n####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")
      #f.writelines("len ==> " + str(len(overview)) + "\n")
      #f.writelines(str(overview))
      #f.close()
      
    except Exception as e:
        outF = open(Sql.areaName+"error.txt","w")
        ausgabe = "Passierte in der CreateMessage.py\n"
        ausgabe += "pokestop_id: " + str(Sql.pokestop_id.__len__) + "\n"
        ausgabe += "name: " + str(Sql.name.__len__) + "\n"
        ausgabe += "latitude: " + str(Sql.latitude.__len__) + "\n"
        ausgabe += "longitude: " + str(Sql.longitude.__len__) + "\n"
        ausgabe += "quest_task: " + str(Sql.quest_task.__len__) + "\n"
        ausgabe += "quest_stardust: " + str(Sql.quest_stardust.__len__) + "\n"
        ausgabe += "quest_pokemon_id: " + str(Sql.quest_pokemon_id.__len__) + "\n"
        ausgabe += "quest_reward_type: " + str(Sql.quest_reward_type.__len__) + "\n"
        ausgabe += "quest_item_id: " + str(Sql.quest_item_id.__len__) + "\n"
        ausgabe += "quest_item_amount: " + str(Sql.quest_item_amount.__len__) + "\n"
        ausgabe += "Wert i" + str(i) + "\n"
        ausgabe += "All Variable: " + str(len(all))
        outF.writelines(ausgabe + str(e))
        outF.close()