# ASL2TXT
SOC project
This project involved a depth understanding of python libraries like numpy, pandas, matplotlib, CV, and later in the final project also neede mediapipe.
It also made me understand the Machine Learning models and their methods of optimization etc.
In the final project I tried to predict the alphabets from the Sign Language Action.
I tried with 2 difffernt models: One was a little bit complex but the other was kind of an easier version of the same. Both used Mediapipe as the major library.
The complex model however didn't work well (both with pytorch and tensorflow). It was underfitting. The accuracy was closed to 3%. Possible reasons were: I was applying too complex model for just predicting a static action as mainly this model
was built to predict a dynamic action like hello and others. I tried to modify it but it didn't work.
However the simpler module works fine and is easier to predict with slight amount of errors.
For the future I am thinking of learning YOLO and use that to predict the sign language, I am currently learning that and hope to learn it sooner.
Also will look into the exact details of why this model was not working and how I can make it work. One thing I'm sure is it will work perfectly fine with dynamic actions like saying Hello,love you etc.
