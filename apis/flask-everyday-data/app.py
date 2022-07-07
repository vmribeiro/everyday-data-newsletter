from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.ControllerUsuario import ControllerUsuario
from controller.ControllerNewsletters import ControllerNewsletters
 


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
 
 
 

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'page': 'home_page'
    })
 

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'members': {'did_it_work': 'Yes!'}
    })



'''
*******************
USERS
*******************
'''

@app.route('/insert_user', methods=['POST'])
def insert_user():

    post_data = request.get_json(silent=True)
    
    result = ControllerUsuario().insertUser(  post_data.get('email')
                                            , post_data.get('name')
                                            , post_data.get('password')
                                            , post_data.get('profile_name')
                                            , post_data.get('birthday')
                                            , post_data.get('job')            )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})


@app.route('/find_user_by_id/<string:user_id>', methods=['GET'])
def find_user_by_id(user_id):
    
    result = ControllerUsuario().findUserById( user_id )

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})



@app.route('/update_user', methods=['POST'])
def update_user():
    
    post_data = request.get_json(silent=True)
    
    result = ControllerUsuario().updateUser(  post_data.get('id')
                                            , post_data.get('email')
                                            , post_data.get('name')
                                            , post_data.get('password')
                                            , post_data.get('birthday')
                                            , post_data.get('job')
                                            , post_data.get('subscription')            )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})

 
@app.route('/delete_user/<string:user_id>', methods=['GET'])
def delete_user(user_id):
    
    result = ControllerUsuario().deleteUser( user_id )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})

 

@app.route('/find_all_users', methods=['GET'])
def find_all_users():
    
    result = ControllerUsuario().findAllUsers()

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})



'''
*******************
NEWSLETTERS
*******************
'''

@app.route('/insert_newsletter', methods=['POST'])
def insert_newsletter():

    post_data = request.get_json(silent=True)
    
    result = ControllerNewsletters().insertNewsletter(  post_data.get('user_id')
                                                      , post_data.get('title')
                                                      , post_data.get('text')
                                                      , post_data.get('banner_url')
                                                      , post_data.get('category')          )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})


@app.route('/find_newsletter_by_id/<string:newsletter_id>', methods=['GET'])
def find_newsletter_by_id(newsletter_id):
    
    result = ControllerNewsletters().findNewsletterById( newsletter_id )

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})



@app.route('/update_newsletter', methods=['POST'])
def update_newsletter():

    post_data = request.get_json(silent=True)
    
    result = ControllerNewsletters().updateNewsletter(    post_data.get('newsletter_id')
                                                        , post_data.get('title')
                                                        , post_data.get('text')
                                                        , post_data.get('banner_url')
                                                        , post_data.get('category')    )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})


@app.route('/delete_newsletter/<string:newsletter_id>', methods=['GET'])
def delete_newsletter(newsletter_id):
    
    result = ControllerNewsletters().deleteNewsletter( newsletter_id )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})

 

@app.route('/find_all_newsletters', methods=['GET'])
def find_all_newsletters():
    
    result = ControllerNewsletters().findAllNewsletters()

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})





if __name__ == '__main__':
    app.run()