let imageName = document.querySelectorAll(".imgName");
  let cardsBottom = document.querySelectorAll(".animationBox.bottom > div");
  let heartIcons = document.querySelectorAll("figure figcaption");
  let fake = document.querySelectorAll(".fake");
  let counterdivs = document.querySelectorAll(
    ".animationBox.top .imgName ~ p b:first-child"
  );
  let _1st = 1000,
    _2nd = 3200,
    _3rd = 5000;

  function resetFake() {
    fake.forEach((elem) => {
      elem.style.opacity = 1;
      elem.style.transform = "translate(0, 0)";
    });
  }

  function x() {
    //  1st element
    anime({
      targets: imageName[0],
      translateX: [-20, 0],
      opacity: [0.5, 1],
      duration: 1500,
    });

    // 2nd element
    anime({
      targets: ".animationBox.top .imgName ~ p",
      scale: [0.8, 1],
      opacity: [0, 1],
      duration: 1000,
      delay: function (el, i) {
        return i * 100 + 300;
      },
    });

    // 2nd element
    anime({
      targets: ".animationBox.headings",
      scale: [0.8, 1],
      opacity: [0, 1],
      duration: 1000,
      delay: function (el, i) {
        return i * 100 + 300;
      },
    });

    // 3rd element
    anime({
      targets: ".animationBox.middle",
      translateY: [40, 0],
      opacity: [0, 1],
      duration: 700,
      delay: 1000,
    });

    // 4th element
    anime({
      targets: cardsBottom[0],
      scale: [0.8, 1],
      opacity: [0, 1],
      duration: 1200,
      delay: 1500,
    });

    // 5th element
    anime({
      targets: cardsBottom[1],
      scale: [0.8, 1],
      opacity: [0, 1],
      duration: 1000,
      delay: 1600,
    });

    // 6th element
    anime({
      targets: cardsBottom[2],
      scale: [0.8, 1],
      opacity: [0, 1],
      duration: 1000,
      delay: 1700,
    });

    // 7th element
    anime({
      targets: heartIcons,
      translateY: [20, 0],
      opacity: [0, 1],
      duration: 1000,
      delay: function (el, i) {
        return i * 100 + 1700;
      },
    });

    // 8th element
    anime({
      targets: fake[2],
      translateX: [0, 60],
      translateY: [0, -140],
      opacity: [1, 0],
      duration: 700,
      delay: 3000,
      easing: "easeOutQuart",
    });

    anime({
      targets: fake[1],
      translateX: [0, 160],
      translateY: [0, -140],
      opacity: [1, 0],
      duration: 700,
      delay: 3000,
      easing: "easeOutQuart",
    });

    setTimeout(() => {
      counterdivs[2].textContent = _3rd + 1;
    }, 3500);

    setTimeout(() => {
      counterdivs[2].textContent = _3rd + 2;
    }, 3550);

    setTimeout(() => {
      counterdivs[2].textContent = _3rd + 3;
    }, 3600);

    anime({
      targets: fake[0],
      translateX: [0, 200],
      translateY: [0, -140],
      opacity: [1, 0],
      duration: 700,
      delay: 3000,
      easing: "easeOutQuart",
      complete: function () {
        resetFake();
        anime({
          targets: fake[1],
          translateX: [0, 160],
          translateY: [0, -140],
          opacity: [1, 0],
          duration: 700,
          delay: 500,
          easing: "easeOutQuart",
        });

        setTimeout(() => {
          counterdivs[1].textContent = _2nd + 1;
        }, 800);

        setTimeout(() => {
          counterdivs[1].textContent = _2nd + 2;
        }, 900);

        anime({
          targets: fake[0],
          translateX: [0, 140],
          translateY: [0, -140],
          opacity: [1, 0],
          duration: 700,
          delay: 500,
          easing: "easeOutQuart",
          complete: function () {
            resetFake();

            setTimeout(() => {
              counterdivs[0].textContent = _1st + 1;
            }, 900);

            anime({
              targets: fake[0],
              translateX: [0, 220],
              translateY: [0, -140],
              opacity: [1, 0],
              duration: 1000,
              delay: 500,
              easing: "easeOutQuart",
              complete: function () {
                anime({
                  targets: "section.animationWrapper span:first-child",
                  height: [0, "100%"],
                  width: [0, "100%"],
                  easing: "easeOutQuart",
                  duration: 500,
                  delay: 500,
                  complete: function () {
                    setTimeout(() => {
                      document.querySelector(
                        "section.animationWrapper span:first-child"
                      ).style.width = 0;
                      document.querySelector(
                        "section.animationWrapper span:first-child"
                      ).style.height = 0;
                      counterdivs[0].textContent = _1st;
                      counterdivs[1].textContent = _2nd;
                      counterdivs[2].textContent = _3rd;
                      x();
                    }, 1000);
                  },
                });
              },
            });
          },
        });
      },
    });
  }

  x();