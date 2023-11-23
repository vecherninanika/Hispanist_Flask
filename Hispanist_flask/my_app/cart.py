from flask import Blueprint, request, redirect, session

module = Blueprint('cart', __name__, template_folder='Hispanist_Flask/templates/cart', static_folder='static/cart', url_prefix='/')


@module.route('/add_to_cart/<article_id>', methods=['GET', 'POST'])
def add_to_cart(article_id):
    if request.method == 'POST':
        print(213)
        if 'Cart' in session:
            print(214)
            if not int(article_id) in session['Cart']:
                session['Cart'].append(int(article_id))
                session.modified = True
                print(218)
        return redirect(request.referrer)


@module.route('/remove_from_cart/<article_id>', methods=['GET', 'POST'])
def remove_from_cart(article_id):
    if request.method == 'POST':
        item = session['Cart'].remove(int(article_id))
        session.modified = True
    return redirect(request.referrer)
