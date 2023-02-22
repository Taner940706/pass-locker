# Pass Locker - Django Framework with Crispy Forms and API (with Django Rest Framework)
## Business logic
,,Pass Locker" is a system for password management, built on Django Framework and crispy forms. The software is designed for all kind of business with many employees.
The system contains information about applications with their username and password for logged user and grouping with specific names (like a name of department and etc.). One User has many Lockers (application with password and username) and one group has many has many Lockers.
The system allows to create, update and delete users and every user has a permission depends on his role:
  - Admin - superuser, have full CRUD functionalities
  - Department Employee - staff user, have limited CRUD functionalities, only can create lockers and change user his user information.
## Details
,,Pass Locker" is based on Django MTV structure + Crispy Forms with FormHelper (make software more DRY) + HTML + CSS + JavaScript + Bootstrap + DataTables (responsive design) + Chart.js (free JavaScript library for making HTML-based charts) + Django Rest Framework.
  - it has database
The system supports the following operations:
  - Login page: /
  - Registration: /register
  - Dashboard: /profile/:id
  - Edit profile: /profile/:id/edit/
  - Delete profile: /profile/:id/delete
  - Group list: /group/:id
  - Add Group: /group/create
  - Edit Group: /group/:id/edit/
  - Delete Group: /group/:id/delete
  - Add Locker: /locker/create
  - Edit Locker: /locker/:id/edit
  - Delete Locker: /locker/:id/delete
## API:
  - Users list: /api/users/
  - Create user: /api/users/create/
  - Edit user: /api/users/:id/edit/
  - Delete user: /api/users/:id/delete
  - Group list: /api/groups/
  - Create group: /api/groups/create/
  - Edit group: /api/groups/:id/edit/
  - Delete group: /api/groups/:id/delete
  - Lockers list: /api/lockers/
  - Create locker: /api/lockers/create/
  - Edit locker: /api/lockers/:id/edit/
  - Delete locker: /api/lockers/:id/delete
## Screenshots
![login](https://user-images.githubusercontent.com/59261346/219965445-3d80437b-c789-42d7-a450-731422b0a5d3.png)
![register](https://user-images.githubusercontent.com/59261346/219965457-4e063945-1fc3-4fd0-90c1-9369253b8d98.png)
![edit_user](https://user-images.githubusercontent.com/59261346/219965513-4ec3721b-c32d-4b4d-85e3-e55351461ec0.png)
![delete_user](https://user-images.githubusercontent.com/59261346/219965518-1435d412-8279-4f65-901c-7ec3fd214d34.png)
![dashboard](https://user-images.githubusercontent.com/59261346/219965537-24704afb-f4a6-48b0-ae20-78bed5d3c727.png)
![create_group](https://user-images.githubusercontent.com/59261346/219965698-0c0a678c-0347-4b5d-bdf8-adacedc46243.png)
![edit_group](https://user-images.githubusercontent.com/59261346/219965706-6d3d0b76-b2fb-4e4f-9131-683877b5355a.png)
![delete_group](https://user-images.githubusercontent.com/59261346/219965716-a20eccfd-3b2f-4ee6-908b-2c1c8cad06d5.png)
![group_list](https://user-images.githubusercontent.com/59261346/219965726-90023027-b4b1-4ed9-a952-e4123a4a33de.png)
![create_locker](https://user-images.githubusercontent.com/59261346/219965743-a4ed4c21-f1fc-4868-bda1-472ed64896af.png
![edit_locker](https://user-images.githubusercontent.com/59261346/219965773-93da9378-bb81-4ea5-915e-495aa4b738f5.png)
![delete_locker](https://user-images.githubusercontent.com/59261346/219965779-23b8d2fa-d324-4d44-9876-2b26f9036215.png)
![list_user](https://user-images.githubusercontent.com/59261346/220709114-cf53f038-f5f7-4a0e-970d-b9e191a35170.png)
![create_user](https://user-images.githubusercontent.com/59261346/220709185-e71b0641-865f-4da4-b314-06924aaa2421.png)
![edit_user](https://user-images.githubusercontent.com/59261346/220709268-2c0f4e6a-87d1-465d-946e-15786fc2d9ed.png)
![delete user](https://user-images.githubusercontent.com/59261346/220709362-8d7d29db-c348-4745-9286-aecf8907ea6d.png)
![list group](https://user-images.githubusercontent.com/59261346/220709479-1e5b2505-18ec-4eb1-8b0b-08b4993688ef.png)
![create group](https://user-images.githubusercontent.com/59261346/220709410-2db6c4c7-22a4-41af-bc92-8826fc99e1b0.png)
![edit group](https://user-images.githubusercontent.com/59261346/220709568-92319eb5-9f15-4cb7-98e9-ed46a530a75f.png)
![delete group](https://user-images.githubusercontent.com/59261346/220709598-e26cdbe4-2c8e-458e-8a87-5502d1fcbc8d.png)
![list locker](https://user-images.githubusercontent.com/59261346/220709657-992b09db-4b05-424d-b656-bc001569ef81.png)
![create locker](https://user-images.githubusercontent.com/59261346/220709682-2fa62886-1c91-4861-8c74-631ef5129b3a.png)
![edit locker](https://user-images.githubusercontent.com/59261346/220709715-526f049e-2c56-4738-980d-750de6dd4b5c.png)
![delete locker](https://user-images.githubusercontent.com/59261346/220709769-0a5d474e-e037-4f30-86ec-031362eb9fd4.png)
