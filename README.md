## fake-progressbar
>Just a fake progress bar :P  
 
Wrap it inside of a loop and call ```progressBar``` providing the required arguments (current processed number and total number to be processed)  
```Python
for i in range(total+1):
    progressBar(i, total)
```
