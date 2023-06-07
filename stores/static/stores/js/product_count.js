const incrementBtn = document.getElementById("increment_btn")
const decrementBtn = document.getElementById("decrement_btn")
const countDiv = document.getElementById("product_count")
const price = countDiv.dataset.productPrice
const subTotalPriceSpan = document.getElementById("sub_total_price")
const totalPriceSpan = document.getElementById("total_price")

const buyQuantity = document.querySelector("input[name='input_quantity']")

let count = 1
let subTotalPrice = price
let totalPrice = price

// + 버튼 클릭 시 count 숫자 증가
incrementBtn.addEventListener("click", () => {
  count++;
  countDiv.textContent = count
  buyQuantity.value = count

  subTotalPrice = count * price
  totalPrice = count * price

  subTotalPriceSpan.textContent = subTotalPrice.toLocaleString()
  totalPriceSpan.textContent = totalPrice.toLocaleString()
})

// - 버튼 클릭 시 count 숫자 감소
decrementBtn.addEventListener("click", () => {
  if (count > 1) { // 현재 숫자가 1보다 큰 경우에만 감소
    count--;
    countDiv.textContent = count
    buyQuantity.value = count

    subTotalPrice = count * price
    totalPrice = count * price

    subTotalPriceSpan.textContent = subTotalPrice.toLocaleString()
    totalPriceSpan.textContent = totalPrice.toLocaleString()
  }
})
