from User import db
# Make a class for our products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    image = db.Column(db.BigInteger,nullable=False)
    
    # Method to remove products we could remove it directly without using a method but to just practice class methods 
    def delete_product(self,product):
        db.session.delete(product)
        db.session.commit()
        return self.product_name