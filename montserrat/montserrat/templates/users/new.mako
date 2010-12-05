<%inherit file="/common/base.html" />

<%def name="title()">Register</%def>


<form method="post" action="/users/create" class="registerForm">
  <div>
    <label for="user_type">User Type:</label>
    <input type="radio" value="scholar" name="user_type" /> Scholar 
    <input type="radio" value="donor"   name="user_type" /> Donor
  <div>
    <label for="firstname">First Name:</label>
    <input type="text" class="input" name="firstname" />
  </div>
  <div>
    <label for="lastname">Last name:</label>
    <input type="text" class="input" name="lastname" />
  </div>
  <div>
    <label for="username">Username:</label>
    <input type="text" class="input" name="username" />
  </div>
  <div>
    <label for="email">E-mail:</label>
    <input type="text" class="input" name="email" />
  </div>
  <div>
    <label for="password">Password:</label>
    <input type="password" class="input" name="password" />
  </div>
    <div><input type="submit" value="Register" /> </div>
  </div>
</form>
