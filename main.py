print("Wait While We Load Import !!!")
from modules.handle_imports import *
from modules.traffic.extract_vehicles import get_plates_in_csv
from modules.traffic.add_missing_data import get_interpolated_csv
from modules.traffic.visualize import  lets_visualize
print("All Imports Done !!")


# Get input file path from user
input_file = input("Enter Filepath of Video: ").strip()

# Check if the provided file path is valid and points to a file
if os.path.isfile(input_file):
    video_path = input_file
# Check if it's a folder or invalid input, then try to find the file in './testData/input'
elif os.path.isdir(input_file) or input_file == "":
    # Use the default sample.mp4 if no filename is provided or the input is a directory
    video_path = "./testData/input/sample.mp4"
# Check if a file with the given name exists in the './testData/input/' directory
elif os.path.isfile(
    os.path.join(os.getcwd(), "testData", "input", os.path.basename(input_file))
):
    video_path = os.path.join(
        os.getcwd(), "testData", "input", os.path.basename(input_file)
    )
# If all checks fail, fall back to the default sample file
else:
    video_path = "./testData/input/sample.mp4"

# Print the determined video path
print(f"Using video file: {video_path}")

video_name = os.path.splitext(video_path)[0].split('/')[-1:][0]
print(video_name)

try:
    csv_output = get_plates_in_csv(video_path, video_name)
    a= True
    print("Extracted Normal CSV")
except Exception as e:
    a=False
    print("Error While Parsing Video : ", e)
if a==True:
    try:
        interpolated_csv = get_interpolated_csv(csv_output, video_name)
        b= True
        print("Congrats, Your CSV is great!!")
    except Exception as e:
        b= False
        print("Error While Making CSV Great : ", e)
if a and b:
    try:
        donee = lets_visualize(interpolated_csv, video_path, video_name)
        if os.name=='nt':
            os.system("cls") 
        else:
            os.system("clear")   
        print("Most Probably your output video is at : ", donee)
    except Exception as e:
        print("Error while inserting data into output Video : ", e)
else:
    print("There were some errors previously, So Find out yourselves.")