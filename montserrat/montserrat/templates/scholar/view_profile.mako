

<%inherit file="/common/base.html" />

<%def name="title()">Scholar Profile View</%def>

<div>
    <div class="profile-user-info">
    <h2>${c.profile_owner.firstname} ${c.profile_owner.lastname}</h2>
    <table>
        <tr>
            <td>Hometown</td>
            <td>${c.profile.hometown}</td>
        </tr>
        <tr>
            <td>School</td>
            <td>
                % if c.profile.school :
                    ${c.profile.school.name}
                % endif
            </td>
        </tr>
        <tr>
            <td>Major</td>
            <td>${c.profile.major}</td>
        </tr>
        <tr>
            <td>GPA</td>
            <td>${c.profile.gpa}</td>
        </tr>
    </table>
    </div>
    <img src="/placeholder.jpg" style="height:250px; width:250px; margin:15px;" />
</div>
