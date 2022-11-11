CREATE DATABASE ESGManagementSoftware
use ESGManagementSoftware

create table Finalapproverprofile(
inputfirstnamet varchar(50) not null, --Name
inputlastnamet varchar(50) not null, --Name
idtutor int not null primary key,
inputemailt varchar(100) not null , --Email address
inputphonet numeric(15) not null, --Phone
inputtypet varchar(25) not null, --Category

);

create table Finaluserprofile(
    
inputfirstnamestu varchar(50) not null, --TutorName
inputlastnamestu varchar(50) not null, --TutorName
idstudent int not null primary key,
inputemailstu varchar(100) not null, --TutorEmail address
inputphonestu numeric(15) not null, --Phone

);

create table Finaluserregister(
registernewid numeric(20) not null,
registernewcontact numeric(15) not null, --StudentName
registernewemail varchar(100) not null primary key, --StudentEmail address
studentnotetotutor varchar(200) not null, --address
tutoridnew varchar(500) not null,
tutornewemail varchar(300) not null,
coursesregistered varchar(200) not null,

);


create table Esgreporting(
n1 varchar(200) not null,
n2 varchar(200) not null,
n3 varchar(200) not null,
n4 varchar(200) not null,
n5 varchar(200) not null,
n6 varchar(200) not null,
n7 varchar(200) not null,
n8 varchar(200) not null primary key,
n9 varchar(200) not null,
n10 varchar(200) not null,
n11 varchar(200) not null,
n12 varchar(200) not null,
n13 varchar(200) not null,
n14 varchar(200) not null,
n15 varchar(200) not null,
n16 varchar(200) not null,
n17 varchar(200) not null,
n18 varchar(200) not null,
n19 varchar(200) not null,
n20 varchar(200) not null,
n21 varchar(200) not null,
n22 varchar(200) not null,
n23 varchar(200) not null,
n24 varchar(200) not null,
n25 varchar(200) not null,
n26 varchar(200) not null,
n27 varchar(200) not null,
n28 varchar(200) not null,
n29 varchar(200) not null,
n30 varchar(200) not null,
n31 varchar(200) not null,
n32 varchar(200) not null,
n33 varchar(200) not null,
n34 varchar(200) not null,
n35 varchar(200) not null,
n36 varchar(200) not null,
n37 varchar(200) not null,
n38 varchar(200) not null,
n39 varchar(200) not null,
n40 varchar(200) not null,
n41 varchar(200) not null,
n42 varchar(200) not null,
n43 varchar(200) not null,
n44 varchar(200) not null,
n45 varchar(200) not null,
n46 varchar(200) not null,
n47 varchar(200) not null,
n48 varchar(200) not null,
n49 varchar(200) not null,
n50 varchar(200) not null,
n51 varchar(200) not null,
n52 varchar(200) not null,
n53 varchar(200) not null,
n54 varchar(200) not null,
n55 varchar(200) not null,
n56 varchar(200) not null,
n57 varchar(200) not null,
n58 varchar(200) not null,
n59 varchar(200) not null,
n60 varchar(200) not null,
n61 varchar(200) not null,
n62 varchar(200) not null,
n63 varchar(200) not null,
n64 varchar(200) not null,
n65 varchar(200) not null,
n66 varchar(200) not null,
n67 varchar(200) not null,
n68 varchar(200) not null,
n69 varchar(200) not null,
n70 varchar(200) not null,
n71 varchar(200) not null,
n72 varchar(200) not null,
n73 varchar(200) not null,
n74 varchar(200) not null,
n75 varchar(200) not null,
n76 varchar(200) not null,
n77 varchar(200) not null,
n78 varchar(200) not null,
n79 varchar(200) not null,
n80 varchar(200) not null,
n81 varchar(200) not null,
n82 varchar(200) not null,
n83 varchar(200) not null,
n84 varchar(200) not null,
n85 varchar(200) not null,
n86 varchar(200) not null,
n87 varchar(200) not null,
n88 varchar(200) not null,
n89 varchar(200) not null,
n90 varchar(200) not null,

);





DROP TABLE Finalapproverprofile;
DROP TABLE Finalstudentregister;
DROP TABLE Finaluserprofile;


