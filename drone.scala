class Drone {
  var movement = new Movement
  var snapshot = new Snapshot

  def process(instructor:Char){
  	if (instructor == '^'){
  		movement.moveUp()
  	}else if (instructor == 'v'){
  		movement.moveDown()
  	}else if (instructor == '<'){
  		movement.moveLeft()
  	}else if (instructor == '>'){
  		movement.moveRight()
  	}else if (instructor == 'x'){
  		snapshot.billboardShot(movement)
  	}else{
  	  println("cann't recognise the instructor: " + instructor)	
  	}
  }
  
  def getCoordinate():Tuple2[Int, Int]={
    val xCoordinate = movement.x
    val yCoordinate = movement.y

    val coordinate = (xCoordinate, yCoordinate)

    return coordinate 
  }

}