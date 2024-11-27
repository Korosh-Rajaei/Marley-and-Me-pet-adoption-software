import os
import pytest
import cohere
from cohere import Client
from DescriptionGenerator import DescriptionGeneratorClass
from DescriptionGenerator import DescriptionGenerationError
from TextFilesMod import TextFilesModClass    
def test_IntegrationDescGenr():
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
    #check if file is there:
    TextFileEdit=TextFilesModClass()
    valid_path="DescGenerHist.txt"
    assert TextFileEdit.OpenTextFile(valid_path) #valid input,should work; otherwise stop testing
    #creating another description to save in dataset; this is not the main one, it is only here to test interference of descriptions! 
    generated_description_2= DescGen.generate_pet_description("a cat, seven years old, rescued, vaccinated",cohere_client)
    assert TextFileEdit.WriteTextFile(generated_description_2,valid_path)
    #write new text in the file/dataset
    assert TextFileEdit.WriteTextFile(generated_description,valid_path) #valid input,should work; otherwise stop testing
    search_result=TextFileEdit.SearchTextFile(generated_description,valid_path) #search the file for the specific text/input given
    search_result = search_result
    if search_result == generated_description:
        assert True
    else:
        assert False
    edited_text = generated_description + "editing the saved/genrated description by adding extra info to it"
    edited_gendescription=TextFileEdit.EditingDescription(generated_description,edited_text) #edit the found description
    #editing works? if not stop testing
    if edited_text == edited_gendescription:
        assert True
    else:
        assert False
    assert TextFileEdit.EditDescription(generated_description,edited_gendescription,valid_path) #valid input,should work; otherwise stop testing
    search_edited_result=TextFileEdit.SearchTextFile(edited_gendescription,valid_path) #search for the edited text
    if TextFileEdit.DeletingDescription(search_edited_result,valid_path) == True:
        assert True
    else:
        assert False
    #checking if deleting worked
    search_deleted_result=TextFileEdit.SearchTextFile(edited_gendescription,valid_path)
    if search_deleted_result == False:
        assert True
    else:
        assert False
    #check whether the first text still exists > no intefrenece 
    if TextFileEdit.SearchTextFile(generated_description_2,valid_path) != False:
        assert True
    else:
        assert False 
    if TextFileEdit.DeletingDescription(generated_description_2,valid_path) == True:
        assert True
    else:
        assert False
    TextFileEdit.ClearDatasetFile(valid_path)