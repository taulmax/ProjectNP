const comments = document.querySelectorAll(".comments__comment");
const showMore = document.querySelector(".comment__main__show-more");
let startNum = 3;

if (comments.length > 3) {
    for (i = 3; i < comments.length; i++) {
        comments[i].style.display = "none";
    }
};

if (comments.length <= 3) {
    showMore.style.display = "none";
}

function showMoreComments() {
    if (comments.length - startNum > 3) {
        for (i = startNum; i < startNum + 3; i++) {
            comments[i].style.display = "flex";
        }
        startNum = startNum + 3;
    } else {
        for (i = startNum; i < comments.length; i++) {
            comments[i].style.display = "flex";
        }
        showMore.style.display = "none";
    }
}

showMore.addEventListener("click", showMoreComments);