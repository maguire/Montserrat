<div id="sidebar-content">
% if 'user' in session :
<h2>Your Account</h2>
<ul>
<li><a href="#">Check your award amount</a></li>
<li><a href="#">Show your contributors</a></li>
<li><a href="#">Retrieve Scholarship Money</a></li>
<li><a href="/users/logout">Logout of your account</a></li>
</ul>
% else :
<h2>Login</h2>
<form method="post" action="/users/dologin">
  <div>
    <div>E-mail:</div>
    <div><input type="text" class="input" name="email" /></div>
  </div>
  <div>
    <div>Password:</div>
    <div><input type="password" class="input" name="password" /></div>
  </div>
  <div>
    <div><input type="submit" value="Sign In" /> </div>
  </div>
</form>

% endif 

</div>
