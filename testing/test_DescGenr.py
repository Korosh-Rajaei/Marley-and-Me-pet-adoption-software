import os
import pytest
import cohere
from cohere import Client
from DescriptionGenerator import DescriptionGeneratorClass
from DescriptionGenerator import DescriptionGenerationError
from TextFilesMod import TextFilesModClass
def test_ConnectToCohere():
    DescGen = DescriptionGeneratorClass()
    wrong_api_1="odkpaodaopksd"
    wrong_api_2=1234567891234567896541236547896541236547
    correct_api = "0njc5ApppXMrxWwOxl2x1PJKm6dvTFjFu8RGx6wI"
    api_list=[wrong_api_1,wrong_api_2,correct_api]
    for i in api_list:
        if DescGen.connect_to_cohere(i) == False:
            assert not(DescGen.connect_to_cohere(i)) 
        else:
            assert True


def test_InfoChecking():
    DescGen = DescriptionGeneratorClass()
    wrong_pet_input_1={'type': 'dog' , 'name':'l' , 'breed':'husky','sex':'m','vacc':'y','color':'white','age':'5'}
    wrong_pet_input_2={'type': 'dog' , 'name':'al' , 'breed':'h','sex':'m','vacc':'y','color':'white','age':'5'}
    wrong_pet_input_3={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'g','vacc':'y','color':'white','age':'5'}
    wrong_pet_input_4={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'m','vacc':'k','color':'white','age':'5'}
    wrong_pet_input_5={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'m','vacc':'y','color':'w','age':'5'}
    wrong_pet_input_6={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'m','vacc':'y','color':'white','age':'five'}
    correct_pet_input={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'m','vacc':'y','color':'white','age':'5'}
    input_testing_examples=[wrong_pet_input_1,wrong_pet_input_2,wrong_pet_input_3,wrong_pet_input_4,wrong_pet_input_5,wrong_pet_input_6,correct_pet_input]
    for i in input_testing_examples:
        if DescGen.InfoChecking(i,"none") == False:
            assert not(DescGen.InfoChecking(i,"none"))
        else:
            assert True

def test_DescGenerator():
    DescGen = DescriptionGeneratorClass()
    co=cohere.Client("0njc5ApppXMrxWwOxl2x1PJKm6dvTFjFu8RGx6wI")
    wrong_prompt_input_1=23983287642
    wrong_prompt_input_2='sdfw;efmwemoqwkmedoqwkdpoqkwdopkq'
    wrong_prompt_input_3=[22,33,44,56,664,234]
    correct_prompt_input_1='the pet is a dog and its name is al. Its sex is: m. This pet is 5 year(s) old. This dog is a husky and its color is white.Vaccination status: y.'
    correct_prompt_input_2={'type': 'dog' , 'name':'james' , 'breed':'pitbull','sex':'male','vacc':'yes','color':'yellow','age':1}
    input_testing_examples = [wrong_prompt_input_1,wrong_prompt_input_2,correct_prompt_input_1,correct_prompt_input_2]
    for i in input_testing_examples:
        if DescGen.generate_pet_description(i,co) == False:
            assert not(False) #DescGen.generate_pet_description(i,co) == False
        else:
            assert True
    with pytest.raises(DescriptionGenerationError):
        coh=cohere.Client("0njc5ApppXMergherhuiiorhFu8RGx6wI") #invalid api or api problems
        DescGen.generate_pet_description('the pet is a dog and its name is al. Its sex is: m. This pet is 5 year(s) old. This dog is a husky and its color is white.Vaccination status: y.',coh)

def test_WriteTextFile():
    text1="Lorem ipsum odor amet, consectetuer adipiscing elit. Consequat vitae hac interdum egestas, ex faucibus euismod. Platea taciti augue interdum hendrerit efficitur aliquet massa diam. Urna accumsan turpis finibus mus etiam."
    text2="the pet is a dog and its name is al. Its sex is: m. This pet is 5 year(s) old. This dog is a husky and its color is white.Vaccination status: y."
    text3="Lorem ipsum odor amet, consectetuer adipiscing elit. Venenatis imperdiet quis nunc sollicitudin lacus facilisi interdum. Non nullam sem placerat class cubilia potenti eget?"
    TextFileEdit=TextFilesModClass()
    TextFileEdit.WriteTextFile(text1,"DescGenerHist.txt")
    TextFileEdit.WriteTextFile(text2,"DescGenerHist.txt")
    TextFileEdit.WriteTextFile(text3,"DescGenerHist.txt")
    f = open("DescGenerHist.txt","r")
    s= f.read()
    assert text1 in s
    assert text2 in s
    assert text3 in s
    f.close()
    assert not(TextFileEdit.WriteTextFile(text1,"notexists.txt"))
    f = open("DescGenerHist.txt","w")
    f.write("")
    f.close()

def test_DeletingDescription():
    text1="Lorem ipsum odor amet, consectetuer adipiscing elit. Consequat vitae hac interdum egestas, ex faucibus euismod. Platea taciti augue interdum hendrerit efficitur aliquet massa diam. Urna accumsan turpis finibus mus etiam."
    text2="the pet is a dog and its name is al. Its sex is: m. This pet is 5 year(s) old. This dog is a husky and its color is white.Vaccination status: y."
    text3="Lorem ipsum odor amet, consectetuer adipiscing elit. Venenatis imperdiet quis nunc sollicitudin lacus facilisi interdum. Non nullam sem placerat class cubilia potenti eget?"
    TextFileEdit=TextFilesModClass()
    f = open("DescGenerHist.txt","a")
    f.write(text1)
    f.write(text2)
    f.write(text3)
    f.close()
    TextFileEdit.DeletingDescription(text1,"DescGenerHist.txt")
    TextFileEdit.DeletingDescription(text2,"DescGenerHist.txt")
    TextFileEdit.DeletingDescription(text3,"DescGenerHist.txt")
    f = open("DescGenerHist.txt","r")
    s= f.read()
    assert not(text1 in s)
    assert not(text2 in s)
    assert not(text3 in s)
    f.close()
    f = open("DescGenerHist.txt","w")
    f.write("")
    f.close()    

def test_ComponentDescGenr():
    DescGen = DescriptionGeneratorClass()
    data_pet_input={'type': 'dog' , 'name':'al' , 'breed':'husky','sex':'m','vacc':'y','color':'white','age':'5'} #valid pet data input
    generated_prompt=DescGen.InfoChecking(data_pet_input,"rescued from accident")
    #does correct input give correct output? if no, stop testing. testing failed
    if generated_prompt != False:
        assert True
    else:
        assert False
    #checking if output is valid and appropriate.if no, stop testing. testing failed
    prompt_check=True
    for i in [data_pet_input['type'],data_pet_input['color'],data_pet_input['breed']]:
        if not(i in generated_prompt):
            prompt_check = False
    assert prompt_check
    user_api = "0njc5ApppXMrxWwOxl2x1PJKm6dvTFjFu8RGx6wI" #valid api
    cohere_client=DescGen.connect_to_cohere(user_api)
    #does correct input give correct output? if no, stop testing. testing failed
    if cohere_client != False:
        assert True
    else:
        assert False

    generated_description= DescGen.generate_pet_description(generated_prompt,cohere_client)
    #does correct input give correct output? if no, stop testing. testing failed
    if generated_description != False:
        assert True
    else:
        assert False
    #checking if output is valid and appropriate. if no, stop testing. testing failed
    if (not(data_pet_input['type'] in generated_description)) and (not(data_pet_input['color'] in generated_description)) and (not(data_pet_input['breed' in generated_description])) and (not("adopt" in generated_description)) and (not("vaccin" in generated_description)):
        assert False
    assert isinstance(generated_description,str)

def test_ComponentDataEditMod():
    #check if file is there:
    TextFileEdit=TextFilesModClass()
    valid_path="DescGenerHist.txt"
    assert TextFileEdit.OpenTextFile(valid_path) #valid input,should work; otherwise stop testing
    #write new text in the file/dataset
    description_text_ex="Meet Al, a charming, 5-year-old male husky with a striking white coat that perfectly matches his lively personality! Al is not just a stunning dog but also fully vaccinated, making him ready for a safe and healthy transition to his new home."
    assert TextFileEdit.WriteTextFile(description_text_ex,valid_path) #valid input,should work; otherwise stop testing
    search_result=TextFileEdit.SearchTextFile(description_text_ex,valid_path) #search the file for the specific text/input given
    search_result = search_result
    if search_result == description_text_ex:
        assert True
    else:
        assert False
    edited_text="Meet Al, a charming, 5-year-old male husky with a striking white coat that perfectly matches his lively personality!"
    edited_description=TextFileEdit.EditingDescription(search_result,edited_text) #edit the found description
    #editing works? if not stop testing
    if edited_text == edited_description:
        assert True
    else:
        assert False
    assert TextFileEdit.EditDescription(description_text_ex,edited_description,valid_path) #valid input,should work; otherwise stop testing
    search_edited_result=TextFileEdit.SearchTextFile(edited_description,valid_path) #search for the edited text
    if TextFileEdit.DeletingDescription(search_edited_result,valid_path) == True:
        assert True
    else:
        assert False
    #checking if deleting worked
    search_deleted_result=TextFileEdit.SearchTextFile(edited_description,valid_path)
    if search_deleted_result == False:
        assert True
    else:
        assert False
    TextFileEdit.ClearDatasetFile(valid_path)
    
        


        
    

    

















