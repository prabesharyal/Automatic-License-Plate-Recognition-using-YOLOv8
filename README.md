# STEPS

## Clone the REPO
```bash 
git clone https://github.com/prabesharyal/DetectLicensePlatefromVideo.git
```

### Copy the path of the repo folder from file explorer
> Looks like this : ```C://User/Downloads/DetectLicensePlatefromVideo/``` 

### Open Anaconda shell and go to the folder by command :
```bash
cd "C://User/Downloads/DetectLicensePlatefromVideo/" 
```

### Create Conda Environment in that folder only:
```ps 
conda create --prefix ./env python==3.10 -y
```

### Activate it 

```ps 
conda activate ./env
```
> __Note__ : _Be in the same directory of git repo and environment_
### Within environment type
```ps 
pip install -r requirements.txt
```

## Run the Script 
```ps 
python main.py
```