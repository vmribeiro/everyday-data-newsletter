from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.ControllerUsuario import ControllerUsuario
 


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


@app.route('/find_user_by_id/<string:user_id>', methods=['POST'])
def find_user_by_id(user_id):
    
    result = ControllerUsuario().findUserById( user_id )

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})

    return jsonify({'DB_DATA': 'deleted_user_{}'.format(user_id)})


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

 
@app.route('/delete/<string:user_id>', methods=['GET'])
def delete_user(user_id):
    
    result = ControllerUsuario().deleteUser( user_id )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})

    return jsonify({'DB_DATA': 'deleted_user_{}'.format(user_id)})
 



if __name__ == '__main__':
    app.run()