import subprocess



#run all allure tests


command = ["pytest", "--alluredir", "allure-results"]
subprocess.run(command)



# run allure server


command2 = "allure serve allure-results"
subprocess.run(command2, shell=True)


