-- *************************************************************
-- CREATE TABLES
-- *************************************************************

DROP TABLE EVERYDAY_DATA.NEWSLETTERS;
DROP TABLE EVERYDAY_DATA.CONTACTS;
DROP TABLE EVERYDAY_DATA.USERS;


CREATE TABLE EVERYDAY_DATA.USERS 
(
	  USER_ID			     SERIAL				PRIMARY KEY
	, USER_EMAIL		     VARCHAR(300)		NOT NULL
	, USER_NAME			     VARCHAR(300)		NOT NULL
	, USER_PASSWORD			 VARCHAR(300)		NOT NULL
	, USER_PROFILE_NAME      VARCHAR(300)		NOT NULL
	, USER_BIRTHDAY		     DATE 				NOT NULL
	, USER_JOB			     VARCHAR(150)		NOT NULL
	, USER_SUBSCRIPTION      CHAR(1)            DEFAULT 		'Y'
);


CREATE TABLE EVERYDAY_DATA.NEWSLETTERS 
(
	  NEWSLETTER_ID			 SERIAL				PRIMARY KEY
	, NEWSLETTER_USER_ID     BIGINT				REFERENCES 		EVERYDAY_DATA.USERS(USER_ID) ON DELETE CASCADE
	, NEWSLETTER_TITLE		 VARCHAR(300)		NOT NULL
	, NEWSLETTER_DATE 		 DATE 				DEFAULT 		CURRENT_DATE
	, NEWSLETTER_TEXT	 	 TEXT				NOT NULL
	, NEWSLETTER_BANNER_URL	 TEXT				NOT NULL
	, NEWSLETTER_CATEGORY	 TEXT				DEFAULT			'GENERAL'
);


CREATE TABLE EVERYDAY_DATA.CONTACTS 
(
	  CONTACT_ID			 SERIAL				PRIMARY KEY
	, CONTACT_USER_ID        BIGINT				REFERENCES 		EVERYDAY_DATA.USERS(USER_ID) ON DELETE CASCADE
	, CONTACT_TITLE		     VARCHAR(300)		NOT NULL
	, CONTACT_DATE 		     DATE 				DEFAULT 		CURRENT_DATE
	, CONTACT_TEXT	 	     TEXT				NOT NULL
	, CONTACT_FILE_URL	     TEXT				
	, CONTACT_FLAG			 VARCHAR(300)		DEFAULT			'SUGGESTION'	
);










-- DUMMY DATA
INSERT INTO EVERYDAY_DATA.USERS       (   USER_EMAIL		
										, USER_NAME			
									   	, USER_PASSWORD
										, USER_PROFILE_NAME 
										, USER_BIRTHDAY			
										, USER_JOB			)
										
VALUES 								  (   'everyday_data@gmail.com'		
										, 'victor_everydaydata'	
									    , 'admin_everydaydata#2022'
										, 'Victor Ribeiro (Everyday Data Administrator)' 
										, TO_DATE('1997-11-21', 'YYYY-MM-DD')			
										, 'Data Analyst at PayPal' 			            );
										

-- CHECKING
--SELECT * FROM EVERYDAY_DATA.USERS;



-- DUMMY DATA
INSERT INTO EVERYDAY_DATA.NEWSLETTERS (     NEWSLETTER_USER_ID   
										  , NEWSLETTER_TITLE		
										  , NEWSLETTER_TEXT	 	
										  , NEWSLETTER_BANNER_URL			)
										
VALUES 								  (     1  
										  , 'Bem-vindo à Everyday Data!'	
										  , '<b>Everyday Data, seu site de notícias do mundo de dados!</b><br> Esse artigo é somente para te dizer: Seja muito bem-vindo! <br> <i>Abraços do tio Victor.</i>'	 	
										  , 'https://i.pinimg.com/736x/1e/06/81/1e0681b8f929a82d9376b10498b8314c.jpg'			);
										

-- CHECKING
--SELECT * FROM EVERYDAY_DATA.NEWSLETTERS;



-- DUMMY DATA
INSERT INTO EVERYDAY_DATA.CONTACTS  (     CONTACT_USER_ID
										, CONTACT_TITLE			
										, CONTACT_TEXT	 	
										, CONTACT_FILE_URL	
										, CONTACT_FLAG					)
										
VALUES 								  (   1   
										, 'Sugestão de artigo sobre BigData'	
										, 'Olá! Gostaria de sugerir que fizessem algum artigo sobre AWS! Podem me chamar em vm.ribeiro@outlook.com para mais detalhes. Abraços!'	 	
										, NULL
										, 'SUGGESTION'					);
										

-- CHECKING
--SELECT * FROM EVERYDAY_DATA.CONTACTS;








