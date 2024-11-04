export const Footer = () => {

    return (
        <>
            <footer className="site-footer">
                <div className="container">
                    <div className="row">
                        {/* Subscribe Form */}
                        <div className="col-md-8">
                            <form action="#" className="subscribe-form">
                                <input type="text" placeholder="Enter your email to subscribe..." />
                                <input type="submit" value="Subscribe" />
                            </form>
                        </div>

                        {/* Social Links */}
                        <div className="col-md-3 col-md-offset-1">
                            <div className="social-links">
                                <a href="#"><i className="fa fa-facebook"></i></a>
                                <a href="#"><i className="fa fa-twitter"></i></a>
                                <a href="#"><i className="fa fa-google-plus"></i></a>
                                <a href="#"><i className="fa fa-pinterest"></i></a>
                            </div>
                        </div>
                    </div>

                    <p className="colophon">Copyright 2024 GroupLions. All rights reserved</p>
                </div>
            </footer>
        </>
    )
}
