

<%inherit file="/common/base.html" />

<%def name="title()">Scholar Profile View</%def>

<div>
    <div>First Name</div>
    <div>
        ${c.profile_owner.firstname}
    </div>
    <div>Last Name</div>
    <div>
        ${c.profile_owner.lastname}
    </div>
    <div>Hometown</div>
    <div>
       ${c.profile.hometown}
    </div>
    <div>School</div>
    <div>
        % if c.profile.school :
            ${c.profile.school.name}
        % endif
    </div>
    <div>Major</div>
    <div>
        ${c.profile.major}
    </div>
    <div>GPA</div>
    <div>
        ${c.profile.gpa}
    </div>
</div>
