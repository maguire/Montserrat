<%inherit file="/common/base.html" />

<%def name="title()">Login</%def>


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
