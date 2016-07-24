import org.scalatest._

class MovementSpec extends FlatSpec {

  def fixture =
    new {
      val movement = new Movement
    }

  // "A movement class" should "start at the coordinate (0,0)" in {
  //   val f = fixture
  //   assert(f.movement.x === 0)
  //   assert(f.movement.y === 0)
  // }

  "A movement class" should "decrease y-coordinate by 1 when move down" in {
    val f = fixture
    f.movement.moveDown()
    assert(f.movement.y === -1)
  }

  it should "increase y-coordinate by 1 when move up" in {
  	val f = fixture
    f.movement.moveUp()
    assert(f.movement.y === 1)
  }

  it should "decrease x-coordinate by 1 when move left" in {
  	val f = fixture
    f.movement.moveLeft()
    assert(f.movement.x === -1)
  }

  it should "increase x-coordinate by 1 when move right" in {
  	val f = fixture
    f.movement.moveRight()
    assert(f.movement.x === 1)
  }

}
