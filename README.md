# Linear-regression-from-scratch
<p>Linear regression is a way to find a line that best fits a set of data points. The line is called the regression line, and it can be used to predict the value of the dependent variable for a given value of the independent variable. </p>

<h2>About the dataset</h2>
<p> The used dataset is a list of tuples created to be used as a toy data.</p>
<em> pst: Make sure to replace it with your dataset. </em>
<br/>
<h2>About the code</h2>
<p> The code cosists from five main functions each will be described bellow:
<ul>
  <li><pre> def fun(x):</pre></li>
  <p> This function defines the predictor or function that we want to apply aka <i>"Linear Function"</i></p>
  <li> <pre>def weightvec():</pre></li>
  <p> This function defines an initial weight so we can use it in our code.  </p>
  <li><pre>def trainLoss(w):</pre></li>
  <p>Which defines the loss function that we'll use, here i've chose to evaluate the performance using mean squre error(MSE). </p>
  <li><pre>def GradientTrainLoss(w):</pre></li>
  <p>This function calculate the gradiant of the loss function to make the needed updates on the weight in the trining process. </p>
  <li><pre>def GradientDescentFun(F, gradientF, weightvec):</pre></li>
  <p> This is the last function that is specified to use all of the functions above.</p>
</ul>
<h2>How I can run the code ?</h2>
<p> Using any of the softwares that can open the notebook file like anaconda and visual studio code or online using google colab.   </p>

<p>For example click on this button:  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/><a href="https://colab.research.google.com/drive/1LV9h--LiKA3lgzChXQiGgamyakaNhJFy?usp=sharing"></a></p>

