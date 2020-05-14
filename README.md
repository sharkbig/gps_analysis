# gps_analysis
Basic GPS Processing Techniques and Tools

## gps analysis is a basic level tool for gps analysis

This pyhton script is used to fo Green Function Curve Fiting:
  The curve is controled by:
  
    1. Linear trend
    2. Seasonal Variation
    3. Coseimic Deformation
    4. Postseismic relaxation
    
  Mathematical expression is as below:
  
    observation=a+bt+sin(2pi*t)+cos(2pi*t)+u(t-teq)+u(t-teq)*(1-exp(teq-t))
  
    where u is the Heaviside fuction (step function)
  
  In order to solve the function and we can linearize as Green Function:
  
  observation = Green Function * coefficient + Error
      O       =       G        *     x       +   e
  
  where O is an nx1 matrix, G is an nxm matrix and x is an mx1 matrix.
  
