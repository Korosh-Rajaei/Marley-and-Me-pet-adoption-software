import cohere
from cohere import Client
class DescriptionGenerationError(Exception):
    """An error related to the API and AI/LLM description generation"""
class DescriptionGeneratorClass:
    """ A class that creates/generates descriptions of pets using GenAI and a LLM powered by Cohere """
    def connect_to_cohere(self, api_key):
        '''
        this function connect to the cohere api and checks if the given api is correct.
        :param: api_key
        :return: true/False
        '''
        if isinstance(api_key,str):
            if len(api_key) == 40:
                
                co = cohere.Client(api_key)
                if co:
                    print("connected to API!")
                    return co
                
                return False
        else:
            print("API is not valid!")
            return False
    def InfoChecking(self,pet_info,other):
        '''
        this function checks whether the given information about the pet is correct and it check for each input type. 
        if all information are correct, then the function return a prompt about the pet's information.
        :param: pet_info, other
        :return: prompt based on info/False
        '''
        final_pet_info={'type': '' , 'name':'' , 'breed':'','sex':'','vacc':'','color':'','age':0}
        situation=True
        problem=''
        desc=""
        strings=['type','name','breed','sex','vacc','color']
        more_than_two_str=['color','type','name','breed']
        try:
            final_pet_info['age']=int(pet_info['age'])
        except ValueError:
            situation = False
            problem="age"
            print("Wrong value for a number variable!")
        for i in more_than_two_str:
            if len(pet_info[i])<2:
                situation = False
                problem=i
            else:
                final_pet_info[i]=pet_info[i]
        if pet_info['vacc'] in ['y','n','None','none','yes','no','Yes','No','']:
            final_pet_info['vacc']=pet_info['vacc']
        else:
            situation = False
            problem='vaccination'

        if pet_info['sex'] in ['m','f','None','none','male','female','Male','Female','']:
            final_pet_info['sex']=pet_info['sex']
        else:
            situation = False
            problem='sex'
        if situation:
            print("All information about pet was in good order. Checking is done!")
            desc= f"the pet is a {final_pet_info['type']} and its name is {final_pet_info['name']}. Its sex is: {final_pet_info['sex']}. This pet is {final_pet_info['age']} year(s) old. This {final_pet_info['type']} is a {final_pet_info['breed']} and its color is {final_pet_info['color']}.Vaccination status: {final_pet_info['vacc']}. Other details: {other}."
            return desc
        else:
            print(f"an entered value was wrong. entered value for {problem} is wrong!  {pet_info}")
            return False
          
    def generate_pet_description(self,pet_details,coh):
        '''
        this function generate the description of the pet.
        :param: pet_details (details of the pet),coh (the cohere server)
        :return: generated_description/ False
        '''
        try:
            if isinstance(pet_details,str) or isinstance(pet_details,str):
                if not('pet' in pet_details) and not('dog' in pet_details) and not('cat' in pet_details) and not('vaccination' in pet_details):
                    return False
                response = coh.generate(
                    model='command-r-08-2024',
                    prompt=f'create a prompt about a pet to be adopted. just give the description text and try to give everything in less than 150 tokens. without any quotation marks (single/double) the details:{pet_details}',max_tokens=250)
                generated_description= response.generations[0].text + ""
                final_description=generated_description.replace("\n"," ")
                return final_description
            else:
                return False
        except:
            raise DescriptionGenerationError("An error has occured which is related to the API or AI/LLM description generation. check your API!")
