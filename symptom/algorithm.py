from account.models import Psychologist, Employee, Client
from scheduler.models import GoesTo
from .models import (
    Symptom,
    PsychologicalDisorder,
    Feel,
    FieldOfExpertise,
    CharacterizedBy,
)

def get_the_psychologist(this_client):
    queryset_feel_symptoms = Feel.objects.filter(client=this_client) # queryset of the sympthoms this client has checked
    list_queryset_feel_symptoms = list(queryset_feel_symptoms)       # list of the queryset  of the sympthoms this client has checked but it needs to be cleared and to consist only symptoms #now it should be a list of objects Feel

    queryset_disorders = PsychologicalDisorder.objects.all()    # queryset of all possible disorders
    list_queryset_disorders = list(queryset_disorders)          #list of objects Disorder
    
    list_feel_symptoms = [list_queryset_feel_symptoms[i].symptom for i in range(0,len(list_queryset_feel_symptoms))] # now it should be only a list of only Symptom objects
 
    disorders_list_scores=[] #list of scores for Disorder objects with same indexes

    for i in range(0,len(list_queryset_disorders)): # going trough all disorders
        score=0
        current_disorder = list_queryset_disorders[i]
        queryset_characterized_by_symptoms=CharacterizedBy.objects.filter(psychological_disorder=current_disorder) #connecting sympthoms with CURRENT disorder
        list_queryset_characterized_by_symptoms=list(queryset_characterized_by_symptoms) #converting queryset to list of objects CharaterizedBy
        list_characterized_by_symptoms = [list_queryset_characterized_by_symptoms[j].symptom for j in range(0,len(list_queryset_characterized_by_symptoms))] # converting that list to a simple list with only Symptom objects

            ######## making scoring algorithm comparing these two lists with only Symptom objects
        if(len(list_feel_symptoms)>len(list_characterized_by_symptoms)):
            for z in range(0,len(list_characterized_by_symptoms)):
                if(list_characterized_by_symptoms[z] in list_feel_symptoms):
                    score+=4
                else:
                    score-=2
            score-=(len(list_feel_symptoms)-len(list_characterized_by_symptoms))/2

        elif(len(list_feel_symptoms)<len(list_characterized_by_symptoms)):
            for z in range(0,len(list_feel_symptoms)):
                if(list_feel_symptoms[z] in list_characterized_by_symptoms):
                    score+=6
                else:
                    score-=2
            score-=(len(list_characterized_by_symptoms)-len(list_feel_symptoms))/2

        else:
            for z in range(0,len(list_feel_symptoms)):
                if(list_feel_symptoms[z] in list_characterized_by_symptoms):
                    score+=8
                else:
                    score-=3

        disorders_list_scores.append(score) #adding current disorder score to the list 

    ###this should return one disorder value on condition that it has maximum score -if there is more than one with the same score it will return first in the list
    most_likely_disorder = list_queryset_disorders[disorders_list_scores.index(max(disorders_list_scores))]


    # now we are trying find all psychologist who have necessery expertise with that disorder
    query_field_of_expertise = FieldOfExpertise.objects.filter(psychological_disorder=most_likely_disorder)
    list_query_field_of_expertise = list(query_field_of_expertise) 

# so the symptoms, diorders will be populated with values that our Psychologist know, so this will never be empty, it has to hit at least one psychologist
    if(len(list_query_field_of_expertise)>1):
        list_foe_psychologist=[list_query_field_of_expertise[i].psychologist for i in range(0,len(list_query_field_of_expertise))] # this is the list of all psychologist with this expertise
        # for i in range(0,len(list_query_field_of_expertise)):
        #     list_foe_psychologist.append(list_query_field_of_expertise[i].psychologist) 

        number_of_clients=[]
        
        for i in range(0,len(list_foe_psychologist)):
            if (GoesTo.objects.filter(psychologist=list_foe_psychologist[i])).exists()==False:
                number_of_clients.append(0)
                continue
            number_of_clients.append(len(list(GoesTo.objects.filter(psychologist=list_foe_psychologist[i])))) #this will return list of integers - number of clients of each psychologist in list_foe_psychologist with same indexes
        
        the_chosen_one = list_foe_psychologist[number_of_clients.index(min(number_of_clients))] #this should return the first psychologist in the list with the lowest number_of_clients
    else:
        the_chosen_one = list_query_field_of_expertise[0].psychologist

    return Psychologist.objects.get(id=the_chosen_one.id) #all in all this should represent the chosen psychologist
