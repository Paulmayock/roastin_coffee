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