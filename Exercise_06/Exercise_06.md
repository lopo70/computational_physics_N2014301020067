# Exercise 06

# Absract
Develop the "super assisted precision strike system".

## Background
* From Newton's second law, we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D0%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-g),<br>
and then write each of these second-order quations as two first-order differential equations<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_x%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D0%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_y%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_y%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g),<br>
finally use the Euler method, we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t).<br>
The drag force on the cannon shell is given by 
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_%7B2%7Dv%5E%7B%7D2), where ![](http://latex.codecogs.com/gif.latex?v%3D%5Csqrt%7Bv_%7Bx%7D%5E%7B2%7D&plus;v_%7By%7D%5E%7B2%7D%7D) is the speed of the shell, and we find<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%5Ctheta%20%3DF_%7Bdrag%7D%28v_x/v%29%3D-B_2vv_x%20%5C%5C%20F_%7Bdrag%2Cy%7D%3DF_%7Bdrag%7Dsin%5Ctheta%20%3DF_%7Bdrag%7D%28v_y/v%29%3D-B_2vv_y),<br>
then we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t).<br>

* If we consider the air density<br>
isothermal model![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0e%5E%7B-y/y_0%7D),<br>
adiabatic model![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%20%7D),<br>
and from ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7DF_%7Bdrag%7D%28y%3D0%29),<br>
we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t).<br>

* If we consider that the acceleration due to gravity, g, depands on altitude, we have<br>
![](http://latex.codecogs.com/gif.latex?g%3Dg_0%28%5Cfrac%7BR%7D%7BR&plus;y%7D%29%5E2)

* If we consider that there exists a headwind, then the drag force become<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3D-B_2%5Cleft%20%7C%20%5Coverrightarrow%7Bv%7D-%5Coverrightarrow%7Bv%7D_%7Bwind%7D%20%5Cright%20%7C%28v_x-v_%7Bwind%7D%29%20%5C%5C%20F_%7Bdrag%2Cy%7D%3D-B_2%5Cleft%20%7C%20%5Coverrightarrow%7Bv%7D-%5Coverrightarrow%7Bv%7D_%7Bwind%7D%20%5Cright%20%7Cv_y)

* The landing point of the shell
Through the calculation, we will get the last point above ground(n) and the point that would have been below ground(n+1). If we let ![](http://latex.codecogs.com/gif.latex?r%3D-y_n/y_%7Bn&plus;1%7D) then a linear interpolation gives<br>
![](http://latex.codecogs.com/gif.latex?x_l%3D%5Cfrac%7Bx_n&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D), and ![](http://latex.codecogs.com/gif.latex?y_l%3D0).
