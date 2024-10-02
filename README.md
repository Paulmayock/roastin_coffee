# Roastin Coffee

Roastin Coffee is currently a fictional coffee website. It is for people interested in coffee and coffee accessories. The purpose of the website is to provide people with the chance to purchase different types of coffee and coffee equipment such as coffee brewers and french presses. A live version can be found here [Roastin Coffee](https://roastin-coffee-847d35823b48.herokuapp.com/)


## E-Commerce Business Model

Roastin Coffee is a B2C type application. The site will sell directly to consumers in small quantities.

## Marketing Strategies.

The concept for Roastin Coffee is a small, local business offering various local produced coffee, therefore the budget for marketing is small.
However, for this type of business where word of mouth is of paramount importance, the obvious choice for marketing is through social media. This will allow the business to be promoted on local community groups with paid options allowing targeted promotion to particular groups of people. A facebook page was created and images of this you will see below. The creation of other social media pages such as Twitter, Instagram and LinkedIn could also be considered.

To keep registered users up to date with changes to the business and new promotions, a regular newsletter would be sent out via email. This would also provide a platform for sponsor information to be distributed to registered users. Signup for the newsletter works through a mailchimp form in the footer of the page.

### Facebook page

![Facebook main page](docs/images/facebook.png)

![Facebook posts](docs/images/facebook_posts.png)

## Planning

### Wireframes

Below is a set of wireframes designs to brainstorm ideas of what the website would look like

![Main page](docs/images/wireframe_main_page.png)

![Products](docs/images/wireframe_products.png)

![Blog](docs/images/wireframe_blog.png)

![Suppliers](docs/images/wireframe_suppliers.png)

### User Stories

As part of the Agile process I created user stories to aid with planning for the project. Although these were added to the project board in the final stages of the project, they were brainstormed before and during the project completion.

### As a User

* I can view what products are availble to purchase.
* I can add choosen products to a shopping cart.
* I can view and update my shopping cart.
* I can make purchases securely.
* I can register to the site.
* I can view and update my profile.
* I can view my order history.
* I can view blog posts.
* I can like/unlike blog posts.
* I can comment and delete my own comments on blog posts.
* I can view the supplliers and their websites.

### Admin

As well as having the same abilities as users, admins also have the additional User Stories.

### As an Admin

* I can create blog posts.
* I can update/delete blog posts.
* I can add new products.
* I can update/delete existing products.
* I can delete user blog comments if inappropriate.
* I can add, edit and delete suppliers info.

### Discarded User Stories

These user/admin user stories unfortunately were dropped due to time constraints.

* As a user I can check a map for cafes nearby.
* As a user I can categorise products by prices and category.
* As a user I can use social platforms to register to the site.


## Database Models

There are several database Models created for the site and the different apps within it.

### Blog Model

#### Post
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    created_on = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(UserProfile, related_name="post_likes",
                                   blank=True)

#### Comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

### Checkout Model

#### Order
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

#### OrderLineItem
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)     

### Contact Model

#### Contact
    """Contact, receive subject from the users """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

### Products

#### Product
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

### Profile Model

#### UserProfile
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

### Suppliers

#### Suppliers
    supplier_name = models.CharField(max_length=100, null=False, blank=False)
    supplier_bio = models.TextField(null=False)
    supplier_image = models.ImageField(null=True, blank=True)
    supplier_website = models.TextField(null=False)

## Website Design

The sites design takes a lot of styling from the Code Institute Boutique Ado follow along lessons. I used the lessons as a base for the website and then added my own styles and models to make the project more of my own work. 

### Main page, header and footer

The header includes the Roastin Coffee name, search bar, nav bar, login button from my account and a cart for how much the items accumulate to in the current cart.
The main screen shows an image of a cup of coffee and beans and adds a nice background so it can give users a good idea of what the websites main business is.
The footer includes contact details, a contact link so users can reach out to the owner, a link to view the business facebook page and a subscription linkso users can subscribe.

![Main header](docs/images/main_header.PNG)

![Main footer](docs/images/main_footer.PNG)

### Products

The products page shows all the products available to be purchased by the user. When a product is clicked the product description is displayed so the user has a better detail fo what type of product they are purchasing. From here the user can choose how many products they wish to purchase.

![Products main page]()
![Products description page]()


### Blog

Users can see blog posts which have been added.

![Blog](docs/images/blog.PNG)

### Suppliers

Users can view where the owner supplies their coffee from, some info about these suppliers and a link which brings the user to the suppliers website.

![Suppliers](docs/images/suppliers_top.PNG)

![Suppliers info](docs/images/suppliers_bottom.PNG)

### Sign up 

Users can sign up using the by clicking on my account and then clicking on register.

![Sign up](docs/images/signup.PNG)

### Sign in

Users can sign in by clicking on my account and then login.

![Sign in](docs/images/signin.PNG)

### Sign Out

Users can sign out using the logout button from the my account logo.

![Logout](docs/images/sign_out.PNG)

### Success message

A message will appear once the user has signed out to show they have signed out successfully.

![Success message](docs/images/success_message.PNG)