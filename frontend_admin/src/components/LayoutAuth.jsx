export default function LayoutAuth({ children }) {
  return (
    <div id="auth">
      <div className="row h-100">
        <div className="col-lg-5 col-12">
          <div id="auth-left">
            <div className="auth-logo">
              <a href="index.html">
                <img
                  src="/images/logo/logo.svg"
                  alt="logo"
                  width={100}
                  height={100}
                />
              </a>
            </div>
            {children}
          </div>
        </div>
        <div className="col-lg-7 d-none d-lg-block">
          <div id="auth-right"></div>
        </div>
      </div>
    </div>
  );
}
